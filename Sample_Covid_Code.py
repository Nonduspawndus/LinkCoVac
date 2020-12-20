import csv
class Details:
    def __init__(self, name, age, contact_number, address, aadhar, vaccinated, answer = "NO"):
        self.name = name
        self.age = age
        self.contact_number = contact_number
        self.address = address
        self.aadhar = aadhar
        self.vaccinated = vaccinated
        self.answer = answer
    def vaccine(self):
        if self.vaccinated == "NO":
            self.answer = "YES"
        else:
            print("Please come after your self quarantine period is over.")
        return self.answer
    def details_file(self):
        return [self.name, self.age, self.contact_number, self.address, self.aadhar, self.answer]
    def aadhar_check(self):
        state = None
        with open('sample_data.csv') as data:
            csv_reader = csv.reader(data)
            for row in csv_reader:
                if row[4] == self.aadhar:
                    return False
        return True
details_list = ''
sen = ''
while True:
    name = input("Enter the name of the Person: ").upper()
    age = input("Enter age: ")
    contact_number = input("Enter contact number: ")
    address = input("Enter address: ")
    aadhar = input("Enter Aadhar Number: ")
    vaccinated = input("Have you been in the contact of a Covid-19 positive patient in the last 14 days? ").upper()
    content = Details(name, age, contact_number, address, aadhar, vaccinated)
    content.vaccine()
    content.aadhar_check()
    details_list = content.details_file()
    if content.aadhar_check() is False:
        break
    else:
        with open("sample_data.csv", "a", newline = '') as file:
            write = csv.writer(file)
            write.writerow(details_list)
    print("Done?")
    sen = input(">>").upper()
    if sen == "YES":
        break
    else:
        continue
