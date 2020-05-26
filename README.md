# coap-server
PhD Work for IoT Class (2020).
## Requisitos

- [Python 2.7.16](https://www.python.org/download/releases/2.7/)
- [CoAPthon](https://github.com/Tanganelli/CoAPthon)
- [Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)

## Instalação

PIP no Debian/Ubuntu
```
$ sudo apt-get install python-pip   #python 2
```

CoAPthon no Debian/Ubuntu
```
$ sudo pip install CoAPthon
```

## Operação

<p align="center">
  <img src="/imgs/diagram.png" width="300">
  <p><em>Diagrama de operação da aplicação com CoAP</em></p>
</p>

### Ambiente



### Servidor

### Cliente

### test.py

Arquivo responsável pela realização dos testes das operações POST, GET e DELETE sem  necessidade do emulador

POST
```
$ python test.py -P POST -p coap://<your-ip-here>:5683/<resource> -P <payload>
```

GET
```
$ python test.py -P GET -p coap://<your-ip-here>:5683/<resource>
```
