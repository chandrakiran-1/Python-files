std={"name":"chandu","age":21,"course":"B.sc"}
print(std)
print(std["name"])
print(std.get("age"))
std["age"]=20
std['city']='hyd'
print(std.keys())
print(std.values())
print(std.items())
print(len(std))
std.setdefault("roll_no",101)
print(std)
std.update({"grade":"A"})
print(std)
for key,values in std.items():
        print(key,":",values)