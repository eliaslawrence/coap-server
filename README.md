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
</p>
<p align="center">
  <em>Diagrama de operação da aplicação com CoAP</em>
</p>

### Ambiente



### Servidor

- Inicializar
```
$ python server.py <your-ip-here> <your-port-here>
```

### Cliente

As aplicações CLIENTE acessam o servidor requisitam os valores dos sensores de temperatura e pressão do AMBIENTE escolhido.

<p align="center">
  <img src="/imgs/sensehat.png" width="300">  
</p>
<p align="center">
  <em>Cliente em estado IDLE</em>
</p>

Caso os valores ultrapassem os limiares predeterminados, os LEDs se acendem na cor vermelha, conforme imagem abaixo.

<p align="center">
  <img src="/imgs/sensehat1.png" width="300">  
</p>
<p align="center">
  <em>Valores de temperatura e/ou pressão acima do THRESHOLD</em>
</p>

Antes de inicializar o programa, o emulador [Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) deve estar rodando na máquina.

- Inicializar
```
$ python client.py <your-ip-here> <your-port-here>
```

O programa irá pedir para que informe o ID do ambiente que deseja vigiar. A seguir, irá pedir que o usuário sete os limiares (THRESHOLD) de temperatura.

Durante a execução do programa, o usuário pode mudar de ambiente ou reconfigurar os THRESHOLDS.

### test.py

Arquivo responsável pela realização dos testes das operações POST, GET e DELETE sem  necessidade do emulador

- POST
```
$ python test.py -P POST -p coap://<your-ip-here>:5683/<resource> -P <payload>
```

- GET
```
$ python test.py -P GET -p coap://<your-ip-here>:5683/<resource>
```
