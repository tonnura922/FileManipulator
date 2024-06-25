import sys

# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python3 file_manipulator.py")
#         sys.exit(1)
#     argment = sys.argv[0]
#     print(argment)

# def reverseFile

class File:
    options = ["reverse","copy","duplicate-content","replace-string"]

    def manipulate(argment):
        if not File.validate(argment):
            print("Your argments are wrong...")
            exit(1)
        else:
            print(File.execute(argment))


        return "finish manupulation"

    def validate(argment):
        
        if len(sys.argv) < 4 or len(sys.argv) >7:
            return False
        
        cmd = sys.argv[1]
        if cmd not in File.options:
            return False

        return True
    
    def execute(argment):
        if argment[1]==File.options[0]:
            print(File.reverse(argment))
        
        elif argment[1]==File.options[1]:
            print(File.copy(argment))

        elif argment[1]==File.options[2]:
            print(File.duplicate(argment))

        elif argment[1]==File.options[3]:
            print(File.replace(argment))
        


        exit(0)

    def reverse(argment):
        input_path = argment[2]
        output_path = argment[3]

        with open(input_path) as f:
            contents = f.read()

        with open(output_path,'w') as f:
            f.write(contents[::-1])

        exit(0)

    def copy(argment):
        input_path = argment[2]
        output_path = argment[3]

        with open(input_path) as f:
            contents = f.read()
            

        with open(output_path,'w') as f:
            f.write(contents)

        exit(0)

    def duplicate(argment):
        input_path = argment[2]
        n = int(argment[3])

        with open(input_path) as f:
            contents = f.read()
            
        with open(input_path,'w') as f:
            print(str(n)+"回複製します")
            for i in range(n+1):
                f.write(contents)

    def replace(argment):
        input_path = argment[2]
        needle = argment[3]
        new_string = argment[4]
        print(needle,new_string)

        with open(input_path) as f:
            contents = f.read()
        new_contents = contents.replace(needle,new_string)
        with open(input_path,'w') as f:
            f.write(contents+'\n'+new_contents)



if __name__ == '__main__':
    print(File.manipulate(sys.argv))
