В docker-compose 2 сервиса - one-node elasticsearch и one-shot python для предзаполнения индекса.  


Питону в command передаются следующие параметры:  

- /app/wait-for-it.sh", "elasticsearch:9200", "--timeout=60",  
Скрипт wait-for-it.sh, рекомендуемый в официальной доке докера (https://docs.docker.com/compose/startup-order/).
Используем его для того, чтобы второй сервис запустился только после того, как эластик начнёт отвечать на порту 9200.  

- "--", "python", "/app/one-shot-python.py", "elasticsearch", "9200", "shakespeare", "shakespeare_data.json"  
После того, как мы убедились, что эластик работает, запускаем второй сервис, которому в параметрах передаём hostname и порт для доступа к elasticsearch, а также название индекса, который будем править и имя json-файла, из которого будем брать данные.
