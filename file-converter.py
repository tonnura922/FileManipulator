import markdown as md
import sys

def convert(argment):
    input_file = argment[2]
    output_file = argment[3]
    with open(input_file) as f:
        contents = f.read()
    with open(output_file,'w') as f:
        html=md.markdown(contents)
        f.write(html)


if __name__ =='__main__':
    convert(sys.argv)