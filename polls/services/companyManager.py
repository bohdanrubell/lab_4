from polls.models import Company


def createCompany(name, speciality, locate):
    obj = Company.objects.create(name=name, speciality=speciality, locate=locate)
    obj.save()
    return obj
