Решение с использованием официальной роли от самих elastic (https://github.com/elastic/ansible-elasticsearch)  
Одна нода - master, 2 других - data.  
- Работоспособность проверял на таких инстансах в GCE: bash$ for i in 0 1 2; do gcloud compute instances create node-${i} --boot-disk-size=10GB --image-family=centos-7 --image-project=centos-cloud --machine-type=n1-standard-1 --tags port9200,port9300 --zone=europe-west4-a; done  
- Качаем роль: ansible-galaxy install elastic.elasticsearch,7.5.2  
- В dependency к роли указано, что используется json_query-фильтр, поэтому на локальной машине нужен jmespath, ставим: sudo apt-get install python-jmespath  
- Запускаем playbook (ansible-playbook -i hosts es-cluster.yml)


Используемые в playbook переменные для конфига:

- cluster.name: "test-cluster"  
имя кластера
  
- node.name: "{{ inventory_hostname }}"  
имя ноды
  
- cluster.initial_master_nodes: "node-0"  
указатель на мастер-ноду
  
- discovery.seed_hosts: "node-0:9300, node-1:9300, node-2:9300"  
указатель на все используемые ноды для поднятия кластера
  
- network.host: "0.0.0.0"  
биндим сервис на всех интерфейсах
  
- http.port: 9200  
входящие http запросы слушаем на 9200
  
- transport.tcp.port: 9300  
ноды общаются по порту 9300
  
- node.data: "{{ data }}"  
является ли нода data-нодой
  
- node.master: "{{ master }}"  
является ли нода master-нодой

## PS:
В случае, если с целевых хостов нет выхода в интернет, а есть только с хоста, на котором выполняется ansible (при этом доступ осуществляется через корпоративный прокси сервер), для работы playbook нужно будет указать в нём прокси-сервер (как описано здесь: https://docs.ansible.com/ansible/latest/user_guide/playbooks_environment.html):  
-  environment:  
     http_proxy: http://proxy.example.com:8080

## PPS:
Понимаю, что playbook получился коротким и не очень информативным. Можно было, конечно, взять ручную установку и описать её самому, но если бы я делал подобную задачу по работе, я бы, вероятно, делал её именно с использованием официальной роли от Elastic, а не строил свой велосипед. Для понимания степени моего знакомства с Ansible можно посмотреть примеры других моих работ-велосипедов с использованием Ansible: https://github.com/migrulos/devops-practice/tree/master/ansible
