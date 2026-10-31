from dataclasses import dataclass
from operator import itemgetter


@dataclass
class DataColumn:
    id: int
    name: str
    size: int
    table_id: int


@dataclass
class DataTable:
    id: int
    name: str


@dataclass
class ColumnTable:
    column_id: int
    table_id: int


tables = [
    DataTable(1, "Клиенты"),
    DataTable(2, "Товары"),
    DataTable(3, "Заказы"),
]

columns = [
    DataColumn(1, "Адрес", 120, 1),
    DataColumn(2, "Артикул", 20, 2),
    DataColumn(3, "Наименование", 80, 2),
    DataColumn(4, "Количество", 4, 3),
]

column_tables = [
    ColumnTable(1, 1),
    ColumnTable(2, 2),
    ColumnTable(3, 2),
    ColumnTable(4, 3),
    ColumnTable(1, 3),
]


def main():
    one_to_many = [
        (column.name, column.size, table.name)
        for column in columns
        for table in tables
        if column.table_id == table.id
    ]

    result_1 = [
        (name, table_name)
        for name, _, table_name in one_to_many
        if name.startswith("А")
    ]

    sizes_by_table = {
        table.id: [
            column.size for column in columns
            if column.table_id == table.id
        ]
        for table in tables
    }
    result_2 = sorted(
        [
            (table.name, min(sizes_by_table[table.id]))
            for table in tables if sizes_by_table[table.id]
        ],
        key=itemgetter(1),
    )

    many_to_many = [
        (column.name, table.name)
        for link in column_tables
        for column in columns
        for table in tables
        if link.column_id == column.id
        and link.table_id == table.id
    ]
    result_3 = sorted(many_to_many, key=itemgetter(0))

    for number, result in enumerate(
        (result_1, result_2, result_3), start=1
    ):
        print(f"Задание В{number}")
        for name, value in result:
            print(f"{name}: {value}")
        print()


if __name__ == "__main__":
    main()
