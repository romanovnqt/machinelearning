country_reader = open("CountryNationalityList/Country.txt", "r")
nationality_reader = open("CountryNationalityList/Nationality.txt", "r")

countrieslist = country_reader.readlines()
nationality_list = nationality_reader.readlines()

for i in range(0, len(nationality_list)):
    nationality_list[i] = nationality_list[i][:len(nationality_list[i])-1]
    countrieslist[i] = countrieslist[i][:len(countrieslist[i]) - 1]
    # print(countrieslist[i])

# print(len(countrieslist))
# for i in range(0,len(countrieslist)):
#     print(countrieslist[i])

# print(len(nationality_list))
# for i in range(0,len(nationality_list)):
#     print(nationality_list[i])

def is_country(token):
    iscountry = False;
    for i in range(0, len(countrieslist)):
        if (" "+ token+" ").find(" "+countrieslist[i]+" ") != -1:
            iscountry = True
    return iscountry

def find_nationality_from_sentence(sentence):
    nationality = "NONE";
    for i in range(0, len(nationality_list)):
        # print(nationality_list[i])
        if (" "+ sentence+" ").find(" "+nationality_list[i]+" ") != -1:
            nationality = nationality_list[i]
    return nationality

def find_countries_from_nationality(nationality):
    country = "NONE"
    for i in range (0,len(nationality_list)):
        if nationality_list[i].find(nationality) != -1:
            country = countrieslist[i]
    return country

# print(find_countries_from_nationality(find_nationality_from_sentence("I'm Vietnamese")))
# print(is_country("Vietnam"))