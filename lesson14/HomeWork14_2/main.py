from student import Student
from group import Group, GroupLimitError

st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
print(gr)


assert gr.find_student("Jobs") == st1  # 'Steve Jobs'
assert gr.find_student("Jobs2") is None

gr.delete_student("Taylor")
print(gr) # Only one student


try:
    for i in range (1, 12):
        st = Student ("Male", 18+i, f"Name{i}", f"Surname{i}", f"RB{i}")
        gr.add_student(st)
except GroupLimitError as e:
    print("Помилка:", e)
print(gr)
print("Кількість у групі: ", len(gr))


assert len(gr.group) == 10
assert gr.find_student("Surname11") is None
