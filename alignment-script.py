import os
import sys
import subprocess


script_arguments = []

for arg in sys.argv:
    script_arguments.append(arg)


#extracting the source and target languages from command line args
l_lang = script_arguments[1][9:-1]
r_lang = script_arguments[3][9:-1]

#first we shall the create the concatenated file in the fast align format - sentence1 ||| sentence 2

# Reading the text files
# argument at index 2 will be the filename of the source language corpus - for the example task it is (English) eng.txt
# argument at index 4 will be the filename of the target language corpus - for the example task it is (Spanish) spa.txt

with open(script_arguments[2], 'r') as l, open(script_arguments[4], 'r') as r:
    l_text = l.read().splitlines()
    r_text = r.read().splitlines()
    l.close()
    r.close()

if len(l_text) != len(r_text):
    sys.exit('Source and target language corpus are not of the same size')

concat_list = [a + " ||| " + b for a,b in zip(l_text, r_text)]

with open('eflomal_input.txt', 'w') as f:
    for line in concat_list:
        f.write(f"{line}\n")
f.close()

#generating alignment data
alignment_indices = subprocess.run(["eflomal-align -i eflomal_input.txt -f eflomal_output.txt"], shell=True, capture_output=True, text=True)
indices = open('eflomal_output.txt', 'r').read().splitlines()
temp = [i.split(' ') for i in indices]
#index = [i.split('-') for i in temp]

c = 0
for i,j in zip(l_text, r_text):
    l_result = subprocess.run([f"echo '{i}' | apertium {l_lang}-tagger"], shell=True, capture_output=True, text=True)
    r_result = subprocess.run([f"echo '{j}' | apertium {r_lang}-tagger"], shell=True, capture_output=True, text=True)
    l_stems = l_result.stdout.split('^')
    r_stems = r_result.stdout.split('^')
    l_stems_pruned = [l_stems[i].strip()[:-1] for i in range(1, len(l_stems)-1)]
    r_stems_pruned = [r_stems[i].strip()[:-1] for i in range(1, len(r_stems)-1)]

    for k in temp[c]:
        print(l_stems_pruned[int(k[0])] + " - " + r_stems_pruned[int(k[2])])
    print('\n')

    c+=1

#cleaning up
os.remove('eflomal_input.txt')
os.remove('eflomal_output.txt')
