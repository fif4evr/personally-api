import sys

def read_file_contents(filename):
    f = open(filename, 'rU')
    filestring = f.read()
    f.close()
    return filestring

def contents_into_list(input_string):
    contents_as_list = []
    for line in input_string.splitlines():
        contents_as_list.append(line)
    return contents_as_list

def analyze_file(contents_as_list):
    test_cases = contents_as_list.pop(0)
    answers_list = []
    for content in contents_as_list:
        line_list = content.split()
        max_shy = int(line_list[0])
        stuff_to_analyze = line_list[1]
        current_count = 0
        additional_needed = 0
        for amount_needed in range(0,max_shy+1):
            if stuff_to_analyze[amount_needed] != '':
                if int(stuff_to_analyze[amount_needed]) > 0 and amount_needed > current_count:
                    additional_needed += (amount_needed - current_count)
                    current_count += amount_needed - current_count
            current_count += int(stuff_to_analyze[amount_needed])
        answers_list.append(additional_needed)
    return answers_list

def write_output(answers_list):
    x = 1        
    file = open("output.txt", "w")
    length = len(answers_list)
    for line in answers_list:
        if x < length:
            output_line = "Case #%d: %s\n" % (x, line)
        else:
            output_line = "Case #%d: %s" % (x, line)
        # print output_line
        file.write(output_line)
        x += 1

    file.close()

def main():
    args = sys.argv[1:]
    filename = args[0]
    file_contents = read_file_contents(filename)
    contents_as_list = contents_into_list(file_contents)
    answers_list = analyze_file(contents_as_list)
    write_output(answers_list)



if __name__ == '__main__':
  main()