import argparse
from reader import read_gdp_data
from report import generate_report


def main():
    parser = argparse.ArgumentParser(description='Анализ CSV файлов')

    parser.add_argument(
        '--files',
        metavar='FILE',
        type=str,
        nargs='+',
        required=True,
        help='CSV файлы для чтения'
    )

    parser.add_argument(
        '--report',
        type=str,
        required=True,
        choices=['average-gdp'],  # можно добавить другие типы отчётов
        help='Тип отчёта'
    )

    args = parser.parse_args()

    # Чтение данных из файлов
    gdp_data = read_gdp_data(args.files)

    # Генерация отчета
    report = generate_report(gdp_data, args.report)

    # Вывод отчета
    print(report)


if __name__ == '__main__':
    main()