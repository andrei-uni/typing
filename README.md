# Клавиатурный тренажёр
Версия 2.2

Авторы: [Лопарев Егор](https://github.com/xyoouy), [Пирогов Андрей](https://github.com/andrei-uni)



## Описание
Данное приложение является реализацией стандартного клавиатурного тренажёра,
которое используется для увеличения скорости печати.


## Требования
* Python версии не ниже 3.6
* PyQt версии 5 с установленным QtWebKit (для *nix-систем нужно устанавливать
  отдельно) для запуска графической версии


## Состав
* Приложение: `App.py`
* Тексты: `Texts/`
* Модули: `Moduls/`
* Музыка: `Music/`



## Графическая версия
Пример запуска: `./App.py`



## Подробности реализации
Модули, отвечающие за статистическую часть, логику рекордов и настройки, расположены в Moduls/.
В основе всего лежат класс `App.Application`, реализующий ввод с клавиатуры и графический интерфейс приложения,
класс `Settings.Settings`, реализующий возможность изменения характеристик игры.
Класс `Records.Records` хранит, сортирует и получает данные класса `RecordType.RecordType`.
За работу статистик отвечают 2 класса: `Accuracy_Statistics.Statistic`(Статистика точности) и
`Speed_Statistics.Statistic`(Статистика скорости).
