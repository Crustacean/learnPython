
def title(name):
    title_name = ""
    if name != None:
        title_name += name[0].upper()

    for i in range(1,len(name)):
        title_name += name[i].lower()

    return title_name

def format_name(f_name, l_name):
    first_name = ""
    second_name = ""

    return f"{title(f_name)} {title(l_name)}"
        
print(format_name("aNGelaa", "mWAIi"))