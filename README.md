# Задание №9

Задание по докеру, кластеризация (счетчик)

```
# Инициализация swarm
$ docker swarm init

logs:
Swarm initialized: current node (jheren476jjjci531zpexv00l) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-29vjt8d4blitvmo6tlrx296kkv17842s0bnwr76m8kuyq1krb8-0irf7hfytyfimp7e0mqrfu9kt 192.168.65.3:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

# Создание сервиса
$ docker service create --name swarmapp --publish published=10000,target=5000 registry:2

logs: 
2xwzvoqutzpf9kx555ldvtepb
overall progress: 1 out of 1 tasks 
1/1: running   [==================================================>] 
verify: Service converged 

# Просмотр созданного сервиса
$ docker service ls

logs:
ID             NAME                     MODE         REPLICAS   IMAGE                              PORTS
ahq9xtv1l6un   registry                 replicated   1/1        registry:2                         *:10000->5000/tcp

# Отправить приложение
$ docker-compose push 

logs:
+] Running 1/9
 ⠿ mongo-swarm Skipped                                                                                                          0.0s
 ⠋ Pushing task-swarm: 65d195dd4a65 Pushed                                                                                      3.9s
 ⠋ Pushing task-swarm: df0478497b3f Pushed                                                                                      3.9s
 ⠋ Pushing task-swarm: d5fd8070b945 Pushed                                                                                      3.9s
 ⠋ Pushing task-swarm: dd7e5e09ba42 Pushed                                                                                      3.9s
 ⠋ Pushing task-swarm: 47c999b3aa43 Pushed                                                                                      3.9s
 ⠋ Pushing task-swarm: 08d2acc3cc4a Pushed                                                                                      3.9s
 ⠋ Pushing task-swarm: 97c7d4b8dd08 Pushed                                                                                      3.9s
 ⠋ Pushing task-swarm: 72e830a4dff5 Pushed  
 
# Создать деплой
$ docker stack deploy --compose-file docker-compose.yml swarmtask9
 
logs:
Ignoring unsupported options: build, restart

Ignoring deprecated options:

container_name: Setting the container name is not supported.

Creating network swarmtask9_default
Creating service swarmtask9_task-swarm
Creating service swarmtask9_mongo-swarm

# Передать переменные окружения 
$ env $(cat .env | xargs) docker stack deploy --compose-file docker-compose.yml swarmtask9 

logs:
Ignoring unsupported options: build, restart

Ignoring deprecated options:

container_name: Setting the container name is not supported.

Updating service swarmtask9_mongo-swarm (id: ndlpdjcnsnxny3doae0udgx48)
Updating service swarmtask9_task-swarm (id: jod6skph574vbj4m1pmzvurnh)

# Результаты после нескольких обращений
$ curl 127.0.0.1:8000

logs: 
Counter: 6 .
```
<img width="470" alt="image" src="https://user-images.githubusercontent.com/72343402/204106544-bd597f05-7c47-437d-aa83-7ab457b75b7e.png">
