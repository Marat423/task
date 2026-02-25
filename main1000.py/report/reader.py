import csv


def read_gdp_data(file_paths):
    """Читает данные о ВВП из нескольких CSV файлов"""
    gdp_by_country = {}

    for file_path in file_paths:
        print(f"Обработка файла: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    country = row['country']
                    gdp = float(row['gdp'])

                    if country not in gdp_by_country:
                        gdp_by_country[country] = []

                    gdp_by_country[country].append(gdp)
        except Exception as e:
            print(f"Ошибка при обработке {file_path}: {e}")

    return gdp_by_country