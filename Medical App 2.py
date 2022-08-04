class Doctor():
    def __init__(self):
        print("This is class Doctor")
        
    def BMI(weight,height):
        bmi = weight/(height*height)
        print("Your Bmi is" + str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Your heart rate is normal!!")
            
        else:
            print("OH SNAP! Your heart rates doesnt seem to be normal. You might have to visit the clinic")
            
class Patient(Doctor):
    def __init__(self,name,weight,height,heart_rates):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rate = heart_rates
    
    def healthCheck(self):
        print("/n Patient's Name :",self.patient_name)
        Doctor.BMI(self.patient_weight,self.patient_height)
        Doctor.heart_rate(self.patient_heart_rate)
        
patient1 = Patient("Micheal",42,0.91444,95)
patient1.healthCheck()
    
patient2 = Patient("Jessica",72,1,103)
patient2.healthCheck()
        
    