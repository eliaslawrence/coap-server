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
  <img src="/imgs/diagram.png" width="800">  
</p>
<p align="center">
  <em>Diagrama de operação da aplicação com CoAP</em>
</p>

### Teste ([test.py](https://github.com/eliaslawrence/coap-server/blob/master/test.py))

Arquivo responsável pela realização dos testes das operações POST, GET e DELETE sem  necessidade do emulador.

- POST
```
$ python test.py -P POST -p coap://<server-ip-here>:<server-port-here>/<resource> -P <payload>
```

- GET
```
$ python test.py -P GET -p coap://<server-ip-here>:<server-port-here>/<resource>
```

### Ambiente ([environment.py](https://github.com/eliaslawrence/coap-server/blob/master/environment.py))

Com a ajuda do emulador [Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat), simula sensores de temperatura e pressão em um determinado ambiente. 

O usuário pode setar um ambiente cujos recursos (temperatura e pressão) já estejam adicionados ao servidor, como também pode criar um novo ambiente.

Um ambiente nada mais é do que uma virtualização dos sensores de temperatura e pressão. Logo, a criação de um ambbiente consiste em adicionar recursos para esses sensores no servidor.

- Inicializar

Antes de inicializar o programa, o emulador [Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) deve estar rodando na máquina. Se for da preferência do usuário, testes podem ser executados através do arquivo [test.py](https://github.com/eliaslawrence/coap-server/blob/master/test.py), sem a necessidade do emulador.

```
$ python environment.py <server-ip-here> <server-port-here>
```

O programa irá pedir para que informe o ID do ambiente ou se deseja criar outro. 

Durante a execução do programa, o usuário pode mudar de ambiente ou criar um outro..

### Servidor ([server.py](https://github.com/eliaslawrence/coap-server/blob/master/server.py))

O servidor é inicializado com apenas um META-resource (ADD) responsável pela criação de novos resources (recursos) referentes aos sensores dos ambientes.

Através de um método POST para o resource '/add' do servidor, passando como payload um ID, estamos, então, criando um novo resource '/<new-id>'. Agora podemos acessar esse novo recurso através dos métodos POST, GET...
  
O servidor escuta as aplicações AMBIENTE, criando recursos para novos sensores e recebendo valores de temperatura e pressão. Por outro lado, recebe requisições das aplicações CLIENTE, requisitando valores de temperatura e pressão de um determinado ambiente.

- Inicializar
```
$ python server.py <server-ip-here> <server-port-here>
```

### Cliente ([client.py](https://github.com/eliaslawrence/coap-server/blob/master/client.py))

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

- Inicializar

Antes de inicializar o programa, o emulador [Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) deve estar rodando na máquina. 

```
$ python client.py <server-ip-here> <server-port-here>
```

O programa irá pedir para que informe o ID do ambiente que deseja vigiar. A seguir, irá pedir que o usuário sete os limiares (THRESHOLD) de temperatura e pressão.

Durante a execução do programa, o usuário pode mudar de ambiente ou reconfigurar os THRESHOLDS.

## Exemplo

- IP do servidor: 192.168.25.4
- Porta do servidor: 5683
- Inicializa servidor

```
$ python server.py 192.168.25.4 5683
```

### Sem emulador para os sensores de temperatura e pressão

- Crie sensor para temperatura com ID **t1**

```
$ python test.py -P POST -p coap://192.168.25.4:5683/add -P t1
```

- Sete temperatura em **t1** para 40 graus

```
$ python test.py -P POST -p coap://192.168.25.4:5683/t1 -P 40
```

- Crie sensor para pressão com ID 'p1'

```
$ python test.py -P POST -p coap://192.168.25.4:5683/add -P p1
```

- Sete pressão em **p1** para 1000 hPa

```
$ python test.py -P POST -p coap://192.168.25.4:5683/p1 -P 1000
```

- A temperatura e pressão podem ser alteradas pelo método POST.

### Com emulador para os sensores de temperatura e pressão

- Inicialize o Sense HAT Emulator 
- Inicialize o simulador de ambiente

```
$ python environment.py 192.168.25.4 5683
```

- A temperatura e pressão podem ser alteradas pelo emulador

### Cliente

- Inicialize o Sense HAT Emulator 
- Inicialize aplicação cliente

```
$ python client.py 192.168.25.4 5683
```

- Sete ID do ambiente: 1
- Sete threshold de temperatura: 50
- Sete threshold de pressão: 1100

Os LEDs não acenderão.

- Sete threshold de temperatura: 30
ou
- Sete threshold de pressão: 900

Os LEDs acenderão.
