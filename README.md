# ansible-monitoring
В плейбук входит деплой Prometheus и Victoriametrics. Основано на [роли prometheus](https://github.com/prometheus-community/ansible/tree/main/roles/prometheus) от prometheus-community и на [роли victoriametrics/single](https://github.com/VictoriaMetrics/ansible-playbooks/tree/master/roles/single) от VictoriaMetrics.

Включает в себя тестирование molecule. Для Victoriametrics написан свой тест по аналогии с тестом Prometheus.

Для Prometheus настроен таргет 0.0.0.0:8428, где висит Victoriametrics.

## Установка зависимостей
```
pip3 install -r requirements.txt
ansible-galaxy install -r roles/prometheus/requirements.yml
```
## Тестирование
Запуск тестирования molecule:
```
cd roles/prometheus
molecule test
```
```
cd roles/victoriametrics
molecule test
```
