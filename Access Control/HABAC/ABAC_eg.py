class User:
    def __init__(self, name, role, department, security_level):
        self.name = name
        self.role = role
        self.department = department
        self.security_level = security_level

class Record:
    def __init__(self, name, classification, department):
        self.name = name
        self.classification = classification
        self.department = department

def can_access(user, record, time_of_day, user_location):
  
    if user.role == 'Doctor' and user.department == record.department:
        if time_of_day == 'business_hours':
            
            if record.classification == 'Sensitive':
                return user.security_level >= 2
            return True

    
    if user.role == 'Nurse' and user.department == record.department:
        if record.classification == 'General' and time_of_day == 'business_hours':
            return True

    return False


dr_alice = User('Dr. Alice', 'Doctor', 'Cardiology', 2)
dr_bob = User('Dr. Bob', 'Doctor', 'Pediatrics', 1)
nurse_carol = User('Nurse Carol', 'Nurse', 'Pediatrics', 1)


record_x = Record('Record X', 'Sensitive', 'Cardiology')
record_y = Record('Record Y', 'General', 'Pediatrics')


print('Dr. Alice accessing Record X:', can_access(dr_alice, record_x, 'business_hours', 'inside'))
print('Dr. Bob accessing Record X:', can_access(dr_bob, record_x, 'business_hours', 'inside'))
print('Nurse Carol accessing Record Y:', can_access(nurse_carol, record_y, 'business_hours', 'inside'))


new_doctor = User('Dr. New', 'Doctor', 'Neurology', 1)
new_record = Record('Record Z', 'General', 'Neurology')

print('New Doctor accessing Record X:', can_access(new_doctor, record_x, 'business_hours', 'inside'))


print('Dr. Alice accessing New Record:', can_access(dr_alice, new_record, 'business_hours', 'inside'))
