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
                        new_node = TreeNode(part, color=Fore.LIGHTBLACK_EX, nodeid=i)
                        current_node.add_child(new_node)
                        current_node = new_node

                    elif current_node.nodeid == 1:
                        new_node = TreeNode(part, color=Fore.LIGHTRED_EX, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node

                    elif current_node.nodeid == 2:
                        new_node = TreeNode(part, color=Fore.LIGHTYELLOW_EX, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node

                    elif current_node.nodeid == 3:
                        new_node = TreeNode(part, color=Fore.LIGHTMAGENTA_EX, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node

                    elif current_node.nodeid == 4:
                        new_node = TreeNode(part, color=Fore.LIGHTCYAN_EX, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node

                        
                    else:
                        new_node = TreeNode(part, color=Fore.LIGHTBLUE_EX, nodeid=current_node.nodeid+1)
                        current_node.add_child(new_node)
                        current_node = new_node


                    
    #for child in root.children:
     #   for j in child.children:
      #      print(j.nodeid)
    return root
        

def print_tree(node, indent="├"):
    if node.nodeid != 0:
        print(node.color + indent + node.name + Style.RESET_ALL)
        

    for child in node.children:
        print_tree(child, indent + "────")

if __name__ == "__main__":    
    urls = []
    lns = ''
    for line in fileinput.input():
        lns = line
        
        #line = line.split('\n')
        #print(line)
        #urls.append(line)
    #urls = open(sys.argv[1]).read().splitlines()
    #urls = sys.stdin.read()
    lns = lns.replace('\\n', ' ').split(' ')
    #print(lns)
    #print(urls)
    root = build_tree_from_urls(lns)
    print_tree(root)

