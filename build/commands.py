class Node:
    def __init__(self, commandName, left=None, right=None, action=None):
        self.commandName = commandName
        self.left = left
        self.right = right
        self.action = action


def clear():
    print("clearing in progress")

def setColor():
    print("couleur")



commands = Node("!"
                , Node("clear", action=clear)
                , Node("set", 
                    Node("color", action=lambda: setColor())
                )
            )



def executeCommand( command):
    command = command.split(" ")
    node = commands
    if command[0] != "!":
        print("command not found")
        return False
    for word in command:
        if word == "!":
            continue
        if node.left and node.left.commandName == word:
            node = node.left
        elif node.right and node.right.commandName == word:
            node = node.right
        else:
            print("command not found")
            return False
    if node.action:
        node.action()
        return True
    else:
        print("command not found")
        return False
