#Brett Sumser

from sys import argv
from BST import BST

def main(argv):
    # Loop over input file (filename passed via argv).
    input_file = argv[1]
    with open(input_file, 'r') as file_ob:
    # Split each line into a task and number (if one exists) 
    #hint: use the split method for strings 
    # Perform the function corresponding to the specified task
    # i.e., insert, delete, inorder, preorder, postorder
    # Close the file when you're done.
        for line in file_ob:
            if ' ' in line:
                command, num = line.split()
                print command
                print num
            else:
                command = line
                BST.traverse(command)
                print command
            #print(line.split()) 
            if 'str' in line:
                break
    pass

if __name__ == "__main__":
    main(argv)

