class Node:
    def __init__(self, commandName, *args, action=None):
        self.commandName = commandName
        self.children = args
        self.action = action


def clear():
    print("clearing in progress")

def setColor():
    print("couleur")


commands = Node("/"
                , Node("clear", action=clear)
                , Node("set", 
                    Node("color", action=lambda: setColor())
                )
            )



def executeCommand(command):
    command = command.split(" ")
    node = commands
    if command[0] != "/":
        print("command not found")
        return False
    for word in command:
        if word == "/":
            continue
        for i in range(len(node.children)):
            if node.children[i] and node.children[i].commandName ==word:
                node = node.children[i]
                break

    if node.action:
        node.action()
        return True
    else:
        print("command not found")
        return False

