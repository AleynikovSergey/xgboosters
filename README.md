# xgboosters

## Features list

* **Feature-1**
  * Система содержит сервер, который слушает входящие соединения от активных датчиков.
  * Протокол включает только входящие данные (от датчика к мониторингу):
    * **Регистрация** 
    ```json
    ({
        "message_type": "register", 
        "payload": sensor_json
    })
    ```
    * **Обновление**
    ```json
    ({
        "message_type": "update", 
        "payload": sensor_json
    })
    ``` 
    * **Снятие с регистрации**
    ```json
    ({
        "message_type": "unregister", 
        "payload": sensor_json
    })
    ``` 
    * Где **sensor_json** - **JSON** объект с параметрами датчиками

* **Feature-2**
  * Система содержит клиент, который может подключаться к пассивным датчикам. 
  * Протокол включает исходящие данные (от мониторинга к датчику):
    * **Запрос**
    ```json
    ({
        "message_type": "request", 
        "payload": sensor_json
    })
    ```
  * Протокол включает входящие данные (от датчика к мониторингу):
    * **Обновление**
    ```json
    ({
        "message_type": "update", 
        "payload": sensor_json
    })
    ```
    * Где **sensor_json** - **JSON** объект с параметрами датчиками

* **Feature-3**
  * Параметры системы хранятся в файле и могут быть изменены через текстовый редактор

* **Feature-4**
  * Cистема отображает на экране перечень датчиков, о которыъ имеет информацию и их параметры: 
    * Статус (***online***/***offline***)
    * Тип
    * Сетевой адрес

* **Feature-5**
  * Система оценивает статус датчика на основе информации, пришедшей от датчика.
  * Если датчик не присылает данные в течение времени, заданного в конфиге для типа датчика, статус выставляется в ***offline***

* **Feature-6**
  * Система на основе данных от датчика может генерировать нотификацию на основе правил, заданных в конфиге для типа датчика

* **Feature-7**
  * Система должна работать только с теми типами датчиков, которые разрешены конфигурацией
* **Feature-8**
  * Система должна поддерживать приём и обработку данных от активного датчика типа ***"чайник"***
* **Feature-9**
  * Система должна поддерживать приём и обработку данных от активного датчика типа ***"холодильник"***
* **Feature-10**
  * Система должна поддерживать приём и обработку данных от активного датчика типа ***"роутер"***
* **Feature-11**
  * Система должна поддерживать запрос и обработку данных от пассивного датчика типа ***"умная розетка"***
* **Feature-12**
  * Система должна поддерживать запрос и обработку данных от пассивного датчика типа ***"входная дверь"***
* **Feature-13**
  * Система должна поддерживать запрос и обработку данных от пассивного датчика типа ***"инфракрасный датчик"***

## Виды устройств
* **Активные**
  * Чайник


## Версии

### 1.1.0

* Добавлена обработка дополнительных метрик от датчиков типов ***"чайник"*** и ***"роутер" ***
  * **Feature-8**
  * **Feature-10**

### 1.0.0

* Реализован сервер, слушающий активные датчики
  * Feature-1
  * Feature-4
* Реализовано зачитывание параметров из конфига
  * Feature-3
* Реализована работа с датчиками типов "чайник" и "роутер"
  * Feature-8
  * Feature-10
* Реализован сброс датчика в offline при срабатывании таймаута на тип датчика
  * Feature-5
* Реализована нотификация в файл на основе правил конфига
  * Feature-6