#!/usr/bin/env python

from resources import Add, Sensor
from coapthon.server.coap import CoAP
import sys


class CoAPServer(CoAP):
  def __init__(self, host, port, multicast=False):
    CoAP.__init__(self,(host,port),multicast)
    
    # CREATE meta-resource: resource used to create resources
    add = Add()
    add.set_server(self)
    self.add_resource('add/',add)
    
    # LOG
    print "CoAP server started on {}:{}".format(str(host),str(port))
    print self.root.dump()

def main():
  ip = sys.argv[1] 
  port = int(sys.argv[2])
  multicast=False

  # CREATE CoAP server
  server = CoAPServer(ip,port,multicast)
  print server

  try:
    server.listen(10)
    print "executed after listen"
  except KeyboardInterrupt:
    print server.root.dump()
    server.close()
    sys.exit()

if __name__=="__main__":
  main()