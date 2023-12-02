listofarms = ('дубинка', 'пистолет', 'автомат')
sec_ranks = ('Охранник', 'Главный Охранник смены', 'Глава департамента охраны')
HR_Ranks = ('Кадровик', 'Глава отдела кадров')
accounting_ranks = ('Главный бухгалтер', 'ГлавБух')
it_ranks = ('Junior', 'Middle', 'Senior')
ranks = (('Охранник', 'Главный Охранник смены', 'Глава департамента охраны'), #0
         ('Кадровик', 'Глава отдела кадров'), #1
         ('Кадровик', 'Глава отдела кадров'), #2
         ('Главный бухгалтер', 'ГлавБух'),    #3
         ('Junior', 'Middle', 'Senior'))      #4


class Person():
    def __init__(self, age, name, gender, salary):
        self.salary = salary
        self.gender = gender
        self.name = name
        self.age = age
        self.role = None
        self.manager = None

    def get_manager(self):
        return self.manager

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_salary(self):
        return self.salary

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_salary(self, salary):
        self.salary = salary

    def set_manager(self, manager):
        self.manager = manager

    def get_rank(self):
        return ranks[self.rankid][self.rank]

    def set_rank(self, rank):
        self.rank = rank

class CEO(Person):
    def __init__(self, age, name, gender, salary):
        super().__init__(age, name, gender, salary)
        self.role = "Глава компании"

class Header_of_Department(Person):
    def __init__(self, age, name, gender, salary):
        super().__init__(age, name, gender, salary)
        self.role = "Глава отдела"

class Accounting(Person):
    def __init__(self, age, name, gender, salary, rank, rankid = 3):
        super().__init__(age, name, gender, salary)
        self.rank = rank
        self.role = ranks[rankid][rank]
        self.rankid = rankid


class Security(Person):
    def __init__(self, age, name, gender, salary, rank, armament, rankid = 0):
        super().__init__(age, name, gender, salary)
        self.armament = armament
        self.rank = rank
        self.role = ranks[rankid][rank]
        self.rankid = rankid

    def get_armament(self):
        for i in range(0, len(listofarms)):
            if i == self.armament:
                return listofarms[i]

    def set_armament(self, armament):
        self.armament = armament

class HR(Person):
    def __init__(self, age, name, gender, salary, rank, rankid = 2):
        super().__init__(age, name, gender, salary)
        self.rank = rank
        self.role = ranks[rankid][rank]
        self.rankid = rankid


class Programmer(Person):
    def __init__(self, age, name, gender, salary, rank, rankid = 4):
        super().__init__(age, name, gender, salary)
        self.rank = rank
        self.role = ranks[rankid][rank]
        self.rankid = rankid

    def get_it_rank(self):
        return it_ranks[self.it_rank]

class OrganizationUnit:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.subunits = []

    def add_organization_unit(self, organization_unit):
        self.subunits.append(organization_unit)

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

    def assign_manager(self):
        self.employees.sort(key=lambda x: x.rank, reverse=True)
        for i in range(1, len(self.employees)):
            self.employees[i].set_manager(self.employees[0])


    def display_structure(self, level = 0):
        print('  ' * level + self.name)
        if len(self.employees) >= 1:
            print(('  ') * (level + 1) + 'Работники отдела:')
        for employee in self.employees:
            if employee.get_manager() != None:
                print('  ' * (level + 1) + str(employee.name + ' - ' + employee.role + ', подчиняется: ' + employee.get_manager().get_name()))
            else:
                print('  ' * (level + 1) + str(employee.name + ' - ' + employee.role))
        for subuint in self.subunits:
            subuint.display_structure(level + 1)


CEO1 = CEO(65, 'Владимир', 'm', '7777777')


company = OrganizationUnit('Rostec')


company.add_employee(CEO1)

finance_department = OrganizationUnit('Финансовый департамент')
administrative_department = OrganizationUnit('Административный отдел')
accounting_department = OrganizationUnit('Бухгалтерия')
head_recruitment_department = OrganizationUnit("Отдел Кадров")
security_departmnet = OrganizationUnit('Служба Безопасности')
it_department = OrganizationUnit('IT Отдел')
administrative_department.add_organization_unit(it_department)

company.add_organization_unit(security_departmnet)


company.add_organization_unit(administrative_department)
company.add_organization_unit(finance_department)
administrative_department.add_organization_unit(head_recruitment_department)
finance_department.add_organization_unit(accounting_department)

#Административный отдел
HD1 = Header_of_Department(40, 'Евгений', 'm', '150000')
administrative_department.add_employee(HD1)

#Охрана

SecOfficer1 = Security(27, 'Кирилл', 'm', '70000', 2, 2)
SecOfficer2 = Security(35, 'Илья', 'm', '130000', 1, 1)
SecOfficer3 = Security(30, 'Валерий', 'm', '50000', 0, 0)
SecOfficer4 = Security(23, 'Антон', 'm', '45000', 0, 0)
SecOfficer5 = Security(22, 'Алексей', 'm', '50000', 0, 0)

security_departmnet.add_employee(SecOfficer1)
security_departmnet.add_employee(SecOfficer2)
security_departmnet.add_employee(SecOfficer3)
security_departmnet.add_employee(SecOfficer4)
security_departmnet.add_employee(SecOfficer5)
security_departmnet.assign_manager()

#Бухгалтерия

Accounter1 = Accounting(35, 'Елена', 'w', '60000', 0)
Accounter2 = Accounting(55, 'Лариса', 'w', '100000', 1)
accounting_department.add_employee(Accounter1)
accounting_department.add_employee(Accounter2)
accounting_department.assign_manager()

#Отдел Кадров
HR1 = HR(40, 'Виктория', 'w', '130000', 1)
HR2 = HR(30, 'Владимир', 'm', '90000', 0)
head_recruitment_department.add_employee(HR1)
head_recruitment_department.add_employee(HR2)
head_recruitment_department.assign_manager()
security_departmnet.assign_manager()

#IT Отдел
Programmer1 = Programmer(43, 'Виталий', 'm', '130000', 2)
Programmer2 = Programmer(23, 'Илья', 'm', '70000', 0)
it_department.add_employee(Programmer2)
it_department.add_employee(Programmer1)
it_department.assign_manager()
HD1.set_manager(CEO1)


company.display_structure()