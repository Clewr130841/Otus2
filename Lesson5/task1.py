def camel2snake(str):
    if(not str or str is None):
        return str
    
    result = [str[0].lower()]
    
    for i in range(1, len(str)):
        ch = str[i]
        if ch.isupper():
            result.append("_")
        result.append(ch.lower())
    return "".join(result)

def snake2camel(str):
    if(not str or str is None):
        return str
    
    result = [str[0].lower()]
    
    nextIsUpper = False
    
    for i in range(1, len(str)):
        ch = str[i]
        if ch == "_":
            nextIsUpper = True
        else:
            if nextIsUpper:
                result.append(ch.upper())
                nextIsUpper = False
            else:
                result.append(ch.lower())
    return "".join(result)

def reverseCase(str):
    if(not str or str is None):
        return str
    
    if(str.find("_") != -1):
        return snake2camel(str)
    else:
        return camel2snake(str)

print(reverseCase("camelCase"))
print(reverseCase("snake_case"))