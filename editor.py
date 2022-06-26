# write your code here
formatters = "Available formatters: plain bold italic header link inline-code new-line unordered-list ordered-list"
commands = "Special commands: !help !done"

def plain(text):
    return text
def bold(text):
    return "**" + text + "**"
def italic(text):
    return "*" + text + "*"
def inline_code(text):
    return "`" + text + "`"
def header(level, text):
    return "#" * level + " " + text + "\n"
def new_line():
    return "\n" 
def link(label, url):
    return f"[{label}]({url})"
def list_(order, rows):
    elements = []
    for i in range(1, rows + 1):
        elements.append(input(f"Row #{i}: "))
    for i in range(len(elements)):
        global text
        if order == "unordered":
            text += "*" + elements[i] + "\n"
        elif order == "ordered":
            text += f"{i + 1}. " + elements[i] + "\n"
    return text
    
    
def formatting(formatter):
    if formatter == "plain":
        text = input("Text: ")
        return plain(text)
    if formatter == "bold":
        text = input("Text: ")
        return bold(text)
    if formatter == "italic":
        text = input("Text: ")
        return italic(text)
    if formatter == "inline-code":
        text = input("Text: ")
        return inline_code(text)
    if formatter == "header":
        level = 0
        while True:
            level = int(input("Level: "))
            if level in range(1, 7):
                break
            else:
                print("The level should be within the range of 1 to 6")
        text = input("Text: ")
        return header(level, text)
    if formatter == "new-line":
        return new_line()
    if formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        return link(label, url)
    if formatter.endswith("list"):
        rows = 0
        while True:
            rows = int(input("Number of rows: "))
            if rows <= 0:
                print("The number of rows should be greater than zero")
                continue
            else:
                break
        if formatter == "unordered-list":
            return list_("unordered", rows)
        if formatter == "ordered-list":
            return list_("ordered", rows)
        
    
    

text = ""
while True:
    user = input("Choose a formatter: ").strip()
    if user == "!done":
        with open("output.md", 'w') as f:
            f.write(text)
        break
    if user == "!help":
        print(formatters)
        print(commands)
    if user not in formatters.split()[2:] and user not in commands.split()[2:]:
        print("Unknown formatting type or command")
    text = text + formatting(user)
    print(text)
