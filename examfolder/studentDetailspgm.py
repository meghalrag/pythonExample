class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Mark:
    def __init__(self,markeng,markmaths):
        self.eng = markeng
        self.maths = markmaths
class Student(Person):
    def __init__(self,nam,age,id,dept,mark):
        Person.__init__(self,nam,age)
        self.id=id
        self.dept=dept
        self.marks=mark
        Student.filesaverFun(self)
    def filesaverFun(self):
        f=open('studentfile.txt','a',1)
        self.fid=str(self.id)+','
        self.fname=self.name+'\n'
        f.write(self.fid)
        f.write(self.fname)
        print 'added successfully'
    def show(self):
        print self.id,'\t',self.name,'\t',self.age,'    \t',self.dept,'\t',self.marks.eng,'        \t',self.marks.maths
        # print self.id,':'
        # print 'id:',self.id
        # print 'name:',self.name
        # print 'age',self.age
        # print 'department:', self.dept
        # print 'mark in maths:',self.mark.maths
        # print 'mark in english:',self.mark.eng
    # def markshow(self):
    #     print 'mark in maths:', self.marks.maths
    #     print 'mark in english:', self.marks.eng
ob=[]
id=0
while 1:
    print 'option:\n1-add Student\n2-display mark with id\n3-display all\n4-Exit'
    x=input('enter your choice')
    if x==1:
        n = input('no:of students:')
        for i in range(n):
            nam=raw_input('enter student name:')
            dept=raw_input('enter department:')
            age=input('age:')
            maths=raw_input('markin maths:')
            eng=raw_input('mark in english:')
            id+=1
            mark1=Mark(eng,maths)
            ob.append(Student(nam,age,id,dept,mark1))
    elif x==2:
        f=open('studentfile.txt','r',1)
        iii=raw_input('enter the stud id:')
        ll=f.readlines()
        for i in range(len(ll)):
            y=ll[i].split(',')
            if y[0]==iii:
                print 'mark in english:',ob[i].marks.eng
                print 'mark in maths:',ob[i].marks.maths
                # print ob[i].markshow()
                break
    elif x==3:
        print 'id\tname\tage\tdepartmnt\tmarkin eng\tmark in maths'
        for i in range(len(ob)):
            ob[i].show()
    elif x==4:
        f=open('studentfile.txt','w',1)
        f.write('')
        break
    else:
        print 'invalid choice'
