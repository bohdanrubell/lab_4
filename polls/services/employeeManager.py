from polls.models import Employee


def createEmployee(company, name, position, salary):
    obj = Employee.objects.create(company=company, name=name, position=position, salary=salary)
    obj.save()
    return obj


def ifExists(company, name, position, salary):
    if Employee.objects.filter(company=company, name=name, position=position, salary=salary).exists():
        return True
    return False


def isHasRightSalary(salary):
    if 100000 < salary or salary < 0:
        return False
    else:
        return True
