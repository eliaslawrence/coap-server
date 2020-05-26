#!/usr/bin/env python

from coapthon.resources.resource import Resource
from coapthon.server.coap import CoAP
import sys

# Sensor resource
class Sensor(Resource):
  def __init__(self,name="Sensor",coap_server=None):
    super(Sensor,self).__init__(name,coap_server,visible=True,observable=True,allow_children=True)
    self.payload = ""
    self.resource_type = "rt1"
    self.content_type = "application/json"
    self.interface_type = "if1"

  # Return payload
  def render_GET(self,request):    
    return self

  # Set payload
  def render_POST(self, request):
    res = self.init_resource(request, Sensor())
    return res

# META Resource
class Add(Resource):
  def __init__(self,name="Add",coap_server=None):
    super(Add,self).__init__(name,coap_server,visible=True,observable=True,allow_children=True)
    self.payload = ""
    self.resource_type = "rt1"
    self.content_type = "application/json"
    self.interface_type = "if1"
    
  def set_server(self, server):
    self.server = server

  def render_POST(self, request):
    resource_id = request.payload
    res = self.server.add_resource(resource_id, Sensor()) # ADD sensor resource to the server 
    return res