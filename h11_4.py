hair = { "black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC" }
shape = { "square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA" }
eye_color = { "blue" : "TTGTGGTGGC", "brown" : "AAGTAGTGAC", "green" : "GGGAGGTGGC" }
gender = { "female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC" }
race = { "white" : "AAAACCTCA", "brown" : "CGACTACAG", "asian" : "CGCGGGCCG" }

suspects = { "Eva" : ['female', 'white', 'blonde', 'blue', 'oval'], "Larisa" : ['female', 'white', 'brown', 'brown', 'oval'],
            "Matej" : ['male', 'white', 'black', 'blue', 'oval'], "Miha" : ['male', 'white', 'brown', 'green', 'square'] }

with open("h11_4.txt", "r") as dna_file:
    dna = dna_file.read()

    suspect = []


    for i in gender:
        if gender[i] in dna:
            suspect.append(i)

    for i in race:
        if race[i] in dna:
            suspect.append(i)

    for i in hair:
        if hair[i] in dna:
            suspect.append(i)

    for i in eye_color:
        if eye_color[i] in dna:
            suspect.append(i)

    for i in shape:
        if shape[i] in dna:
            suspect.append(i)

    for i in suspects:
        if suspects[i] == suspect:
            print(f"The person we are looking for is {i}")