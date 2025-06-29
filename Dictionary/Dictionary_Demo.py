jobList = {"infosys" : "tester", "acpl" : "developer", "pacematic" : "HR"}

# to know the type of class (class is dictionary)
print(type(jobList))

# get the value using get key method
printJob1 = jobList["pacematic"]
print(jobList.get("pacematic"))

# get the value directly
printJob2 = jobList["infosys"]
print(printJob2)

# try to print doens't exist value (facing an error)
# printJob3 = jobList["Roche"]
# print(printJob3)

# add new pair option 1
jobList["TCS"] = "data analytics"
print(jobList)

# add new pair option 2
AddNewJob = jobList.update({"UST" : "Product Manager"})
print(jobList)

# another example of dictionary

employees = {
    "emp_name" : "muskan",
    "emp_age" : 19,
    "emp_role" : "HR",
    "emp_skill" : ["python", "java", "react"]
}


# print the all dictionary
print(employees)

# print the values only keys separately
print(employees.values())
print(employees.keys())

# print the type of emp_skill(list)
skills = employees["emp_skill"]

# print all skill list
print(type(skills))
print(skills)

# print the length of list
len_skill = len(skills)
# option 1
print(f"muskan has {len_skill} skills")
# option 2
print("user has {} skill".format(len_skill))



