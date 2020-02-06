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
Примеры того, что я делал на Ansible, можно посмотреть тут: https://github.com/migrulos/devops-practice/tree/master/ansible
