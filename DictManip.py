myInfo = {
    "name":"Ben",
    "age":"20",
    "home":"in the USA",
    "favorite language":"C#"
}

def printInfo(d):
    for i in d:
        print "My", i, "is", d[i]

printInfo(myInfo)