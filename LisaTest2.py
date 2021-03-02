newlist = []
isNotNull = True
# noinspection PyStatementEffect
while isNotNull == True:
    new_value = int(input("a number here"))
    if new_value == 0:
        isNotNull = False
    else:
        newlist.append(new_value)


print("There is entered array:", newlist)


print(min(newlist), "is the minimal value")


print(max(newlist), "is the maximal value")


print(max(newlist)-min(newlist), "is the difference")
