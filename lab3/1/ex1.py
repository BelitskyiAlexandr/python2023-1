def copy_lines(infile_path, outfile_path, num_lines):
    with open(infile_path, 'r') as infile:
        with open(outfile_path, 'w') as outfile:
            for i in range(num_lines):
                line = infile.readline()
                if not line:
                    break
                outfile.write(line)


infile_path = 'input.txt'
outfile_path = 'output.txt'
num_lines = 5

copy_lines(infile_path, outfile_path, num_lines)
