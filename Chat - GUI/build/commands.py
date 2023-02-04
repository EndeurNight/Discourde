class Node:
    def __init__(self, commandName, *args, action=None):
        self.commandName = commandName
        self.children = args
        self.action = action


def clear(gui):
    print("clearing in progress")
    gui.chat.delete(1.0, "end")

def setColor():
    print("couleur")


commands = Node("/"
                , Node("clear", action=clear)
                , Node("set", 
                    Node("color", action=lambda: setColor())
                )
            )

def executeCommand(command, gui):
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
        node.action(gui)
        return True
    else:
        print("command not found")
        return False

