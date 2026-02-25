Скрипт для обработки CSV файлов с данными о ВВП стран и генерации отчетов.

## 📋 Стек технологий

- **Python 3.8+** - основной язык
- **argparse (stdlib)** - обработка аргументов командной строки
- **csv (stdlib)** - чтение CSV файлов
- **tabulate** - вывод таблиц в консоль
- **pytest** - тестирование
- **pytest-cov** - покрытие кода

## 🚀 Установка

```bash
pip install tabulate pytest pytest-cov
python report/main.py --files data/economic1.csv data/economic2.csv --report average-gdp

📊 Формат CSV файлов
Колонка	Описание
country	Название страны
year	Год
gdp	ВВП
gdp_growth	Рост ВВП (%)
inflation	Инфляция (%)
unemployment	Безработица (%)
population	Население
continent	Континент


Пример CSV файла:
csv
country,year,gdp,gdp_growth,inflation,unemployment,population,continent
United States,2023,25462,2.1,3.4,3.7,339,North America
United States,2022,23315,2.1,8.0,3.6,338,North America
United States,2021,22994,5.9,4.7,5.3,337,North America
China,2023,17963,5.2,2.5,5.2,1425,Asia
China,2022,17734,3.0,2.0,5.6,1423,Asia
China,2021,17734,8.4,1.0,5.1,1420,Asia
Germany,2023,4086,-0.3,6.2,3.0,83,Europe
Germany,2022,4072,1.8,8.7,3.1,83,Europe
Germany,2021,4257,2.6,3.1,3.6,83,Europe