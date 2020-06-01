import CountryNationalityTerminal

csv_file = "test.csv"
raw_csv_file = "raw_"+csv_file
file_reader = open(("DataFile/rawData/"+raw_csv_file), "r") #where file_object is the variable to add the file object.

data = file_reader.readlines()
# print(data)
datalist = list(data)
# print(len(datalist))

negative_words = [" never "," no "," hardly "," sometimes "]

#prep
unneccessary_words = [" to "," used "," in "," the "," a "," an "," at "," on "," in "," about "," the ",
                      " of "," for "," should "," could "," must "," - ", " by "," do "," can "," will "," shall "]

relation_keys = [" died "," born "," established "," enemy "," friend "," played "," invented "," left "," return ",
                 " liberated "," enslaved "," opposed "," supported "," killed "," had "];

tobe_verbs = [" was "," were "," is "," are "," am "]

def convertword(old_sentence,word_startposition,new_word,old_word_length):
    new_sentence = old_sentence[:word_startposition] + new_word + old_sentence[(word_startposition + old_word_length):]
    return new_sentence


def extracttriple(sentence):
    #this function to eliminate unnecsarry words and create list of keywords

    #replace nationality with country
    nationality = CountryNationalityTerminal.find_nationality_from_sentence(sentence)
    if nationality.find("NONE") == -1:
        country = CountryNationalityTerminal.find_countries_from_nationality(nationality)
        sentence = convertword(sentence, sentence.find(nationality), country, len(nationality))

    #eliminate unnecsarry words
    for j in range(0, len(unneccessary_words)):
        unneccessary_word_startposition = (sentence).find(unneccessary_words[j])
        if unneccessary_word_startposition != -1:
            sentence = sentence[:unneccessary_word_startposition] + " " + sentence[(unneccessary_word_startposition + len(unneccessary_words[j])):]

    #replace negative word to "not"
    for j in range(0,len(negative_words)):
        negative_word_startposition = (sentence).find(negative_words[j])
        if negative_word_startposition != -1:
            sentence = sentence[:negative_word_startposition] + " not " + sentence[(negative_word_startposition + len(negative_words[j])):]

    #replace tobe verbs word to "be"
    for j in range(0,len(tobe_verbs)):
        tobe_verbs_startposition = (sentence).find(tobe_verbs[j])
        if tobe_verbs_startposition != -1:
            # sentence = sentence[:tobe_verbs_startposition] + " be " + sentence[(tobe_verbs_startposition + len(tobe_verbs[j])):]
            sentence = convertword(sentence,tobe_verbs_startposition," be ",len(tobe_verbs[j]))

    tokens = sentence.split(" ")

    step = 1
    relation_startingtoken = 0
    tail_startingtoken = 0


    #finding head, relation, tail
    for j in range(0, len(tokens)):
        if step == 1:
            if tokens[j][:1].islower() == True:
                relation_startingtoken = j
                step = step + 1

        else:
            if step == 2:
                if tokens[j][:1].isupper() == True:
                    tail_startingtoken = j
                    step = step + 1
                else:
                    if tokens[j][:1].isnumeric() == True:
                        tail_startingtoken = j
                        step = step + 1

    sentence = "" + tokens[0]

    for j in range(1, relation_startingtoken):
        sentence = sentence + "_" + tokens[j]
    # sentence = sentence + " " + tokens[relation_startingtoken]

    for j in range(relation_startingtoken, tail_startingtoken):
        if (" "+tokens[j]+" ").find(" be ") == -1:
            sentence = sentence + " " + tokens[j]

    sentence = sentence + " " + tokens[tail_startingtoken]

    ispreviouscountry = False
    if CountryNationalityTerminal.is_country(tokens[tail_startingtoken]) == True:
        ispreviouscountry = True

    for j in range(tail_startingtoken + 1, len(tokens)):
        if CountryNationalityTerminal.is_country(tokens[j])==True:
            sentence = sentence + " " + tokens[j]
            ispreviouscountry = True
        else:
            if ispreviouscountry == True:
                sentence = sentence + " " + tokens[j]
                ispreviouscountry = False
            else:
                sentence = sentence + "_" + tokens[j]


    return sentence
    #end function extracttriple





def printdata():
    for i in range(0, len(datalist)):
        fields = datalist[i].split(",")

        if i>0:
            line = extracttriple(fields[0]) + "," + fields[1]
            print(line)
            # file_writer.write(line)
        else:
            print(datalist[i])
            # file_writer.write(datalist[i])

            # for j in range(0, len(fields)):
            # print(fields[j])
    file_reader.close()


for i in range(0, len(datalist)):
    datalist[i] = datalist[i][:(len(datalist[i])) - 1]
    # print(datalist[i])

# printdata()


