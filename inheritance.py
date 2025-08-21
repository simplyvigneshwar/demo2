class person:
    def __init__(self,name,age):
       self.name=name
       self.age=age
       
    def intro(self):
       return f'My Name is {self.name} and I am {self.age}'
       
       
       
class student(person):
      def __init__(self,name,age,student_id):
         super().__init__(name,age)
         self.student_id=student_id
        
      def studentintroduce(self):
         return f"and iam a student , My student Id is {self.student_id}"
         
s1=student("Vigneshwar",23,19132006)
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
print(s1.studentintroduce())
        