from pydantic import BaseModel ,EmailStr ,Field
class student(BaseModel):
    name:str
    age :int (Field(gt=15 , lt=50))
    email:EmailStr
    #to set the defaukt value u can do :- name:str = "ayush" 
new_student = {"name":"aush" , "age":18 , "email":"aush@example.com"}
new_student2 = {"name":"ayush" , "age":19,"email":"abc@gmail.com"}

student_obj=student(**new_student)
student_obj2=student(**new_student2)
print(student_obj)
print(student_obj2) 
print(student)
