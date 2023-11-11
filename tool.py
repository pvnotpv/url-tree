from colorama import Fore, Style
import sys
import fileinput

class TreeNode:
    def __init__(self, name, color, nodeid):
        self.name = name
        self.color = color
        self.children = []
        self.nodeid = nodeid

    def add_child(self, child_node):
        self.children.append(child_node)

def build_tree_from_urls(urls):
    co = [Fore.GREEN, Fore.RED, Fore.BLUE]
    import random
    root = TreeNode("/", color=Fore.WHITE, nodeid=0)
    i = 1
    
    for url in sorted(urls):
        parts = url.split("/")
        current_node = root

        for part in parts:
            m = random.randint(0,3)
            if part:
                found = False
                for child in current_node.children:
                    if child.name == part:
                        current_node = child
                        found = True
                        break
                
                if not found:
                    if current_node.nodeid == 0:
                        new_node = TreeNode(part, color=Fore.RED, nodeid=i)
                        current_node.add_child(new_node)
                        current_node = new_node

                    elif current_node.nodeid == 1:
                        new_node = TreeNode(part, color=Fore.GREEN, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node

                    elif current_node.nodeid == 2:
                        new_node = TreeNode(part, color=Fore.YELLOW, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node

                    elif current_node.nodeid == 3:
                        new_node = TreeNode(part, color=Fore.WHITE, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node
                        
                    else:
                        new_node = TreeNode(part, color=Fore.MAGENTA, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node


                    
    return root
        

def print_tree(node, indent="├"):
    if node.nodeid != 0:
        print(node.color + indent + node.name + Style.RESET_ALL)
        

    for child in node.children:
        print_tree(child, indent + "──")

if __name__ == "__main__":    
    urls = []
    lns = ''
    for line in fileinput.input():
        lns = line
        
    lns = lns.replace('\\n', ' ').split(' ')
    root = build_tree_from_urls(lns)
    print_tree(root)

