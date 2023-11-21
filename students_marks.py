'''Write a program (WAP) to create a dictionary of
students to store names and marks obtained in 5
subjects.'''


name_and_mark = {
    "ram" : {"englis": 75 , "match" : 60 , "ip" : 70 , "hindi" : 78 , "eco" : 60} ,
    "sayam" : {"englis": 56 , "match" : 75 , "ip" : 79 , "hindi" : 88 , "eco" : 61} 
}
print(name_and_mark.items)
for name,marks in name_and_mark.items():
    print(F"marks obtained by {name}")
    for subject,mark in marks.items():
        print(f"    {subject} : {mark}")