from django.db import models

# Create your models here.

# 병원에 오는 사람들을 기록하는 시스템을 만들려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있는가?
# >> 한 의사는 여러명의 환자를 볼 수 있고, 한 환자는 여러 명의 의사에게 진료 가능
# >> ∴ M:N

class Doctor(models.Model):  # 1번 표
    name = models.TextField()
    
class Patient(models.Model):  # 2번 표
    name = models.TextField()
    #doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')  
    doctors = models.ManyToManyField(Doctor, related_name='patients') 
    # reservation 테이블을 통해서, N:N 관계를 맺겠다
    # related_name = patient_set.all() = 'patients'
    # ∴  doctor1.patient_set.all() = doctor1.patients.all()
        
# Doctor : Reservation = 1:N
# Patient : Reservation = 1: N
# Doctor : Patient = M : N

# class Reservation(models.Model):  # 3번표
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
# 1번과 3번은 1:n , 2번과 3번도 1:n   3번 표는 중간다리

