from tabulate import tabulate


def generate_average_gdp_report(gdp_by_country):
    """Генерирует отчет со средним ВВП по странам"""
    avg_data = []
    for country, gdps in gdp_by_country.items():
        avg_gdp = sum(gdps) / len(gdps)
        avg_data.append([country, avg_gdp])

    avg_data.sort(key=lambda x: x[1], reverse=True)

    table_data = []
    for i, (country, avg_gdp) in enumerate(avg_data, start=1):
        # Используем floatfmt для форматирования чисел в tabulate
        table_data.append([i, country, avg_gdp])

    return tabulate(table_data,
                    headers=[" ", "country", "gdp"],
                    tablefmt="grid",
                    colalign=("right", "left", "right"),
                    floatfmt=".2f")  # Форматируем все числа с двумя знаками


def generate_report(data, report_type):
    """Фабрика для создания различных типов отчетов"""
    if report_type == 'average-gdp':
        return generate_average_gdp_report(data)
    else:
        raise ValueError(f"Неизвестный тип отчета: {report_type}")