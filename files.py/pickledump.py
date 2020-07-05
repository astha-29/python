import pickle,student
f=open("student.dat","wb")
s=student.student(123,"john",90)
pickle.dump(s,f)
f.close()