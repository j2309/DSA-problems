def are_rotational(s1,s2):
#check if legth are not the same
if len(s1)!= len(s2)
#concatenate s1 with itself and check if s2 is a substring
if s2 in(s1+s1):
r eturn true
return false

#example
s1="abcde"
s2="edcsb"
if are_rotational(s1,s2)
print(f"'{s1}and {s2} are are_rotationally equal.")e
else:
print(f"'{s1} and '{s2}' are not rotationally equal.)