def cross_join(employees, departments):
    """
    Реализует декартово произведение списков employees и departments

    :param employees: Список LastName сотрудников таблицы Employee
    :param departments: Список DepartmentName таблицы Department
    :return: Генератор пар (LastName, DepartmentName)
    """
    # put your code here
    result = []
    for emp in employees:
        for dep in departments:
            yield emp, dep

    pass
