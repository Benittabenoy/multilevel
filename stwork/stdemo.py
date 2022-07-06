lst=[10,10,1,12,13,14,15,16,16,16]

st=set(lst)
print(st)

st1={1,2,3,4,5}
st2={10,11,12,2,3}

union_set=st1.union(st2)
print(union_set)

intersection_set=st1.intersection(st2)
print(intersection_set)

diff_set=st1.difference(st2)
print(diff_set)
st3= {100, 200, 300}


students=["ram","ravi","appu","ruby","arun","jhon","tom"]
passed_students=["appu","ravi","jhon"]
st_students=set(students)
st_passed=set(passed_students)
failed=st_students.difference(st_passed)
print(failed)
                    # OR

students=["ram","ravi","appu","ruby","arun","jhon","tom"]
passed_students=["appu","ravi","jhon"]
st_students=set(students)
st_passed=set(passed_students)
fail=st_students-(st_passed)
print(fail)

