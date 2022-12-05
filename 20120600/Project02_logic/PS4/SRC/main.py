from handle_input import handleInput
from resolution import Robinson
from os import walk

inputDir = './PS4/SRC/INPUT'
outputDir = './PS4/SRC/OUTPUT'

def main():
    filenames = next(walk(inputDir), (None, None, []))[2]  # [] if no file

    fileIndex = 0
    for filename in filenames:
        #Step 1: parse input to list of literal and literal negative of alpha
        listLiter, alpha = handleInput(inputDir + '/' + filename)

        #Step 2: merge listLiter and alpha into KB
        out_filename = outputDir + '/output' + str(fileIndex) + '.txt'
        fileIndex += 1
        res = Robinson(out_filename, listLiter, alpha)
        
        #Step 3: Write the result into output
        f = open(out_filename,'a')
        if res: 
            f.write('YES')
        else:
            f.write('NO')

main()
