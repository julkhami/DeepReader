import sys
import json


print("Welcome to DeepReader!")

# Get the name of the text from the command line
text_name = sys.argv[1]

print("You entered this text:")
print(text_name)

# Open the data file. If it doesn't exist, create a new blank file.
f = open("dr.dat")



print("The data file was found and opened.")

# If the file is blank, create a new data list.
data = json.load(f)


print("Data loaded. Here's the first entry:")
print(data[0]["name"])





# We have the data list. Now you can close the file.
f.close()

print("The data file was loaded and the file has now been closed.")

# create a list of texts from the data list
texts_list = []


print("Now iterating through all entries in the data file to see the titles of the texts.")


# go through the data, getting all the names of the text
for item in data:
    



    print("Items:")
    print(item["name"])

    texts_list.append(item["name"])
    print("You addrd this title to your list of text names. This is the list:")

    print(texts_list)







# Check if the new text name is present. If it's not, create new values for the entry values - text name, text and index.
if text_name not in texts_list:






    print("This title was not found in the text list.")




    # Get the text and clean out blank newlines
    text = open(text_name).read().splitlines()
    lines = []
    for line in text:
        if line != "":
            lines.append(line)



    # Set the index to zero
    index = 0



    data.append({"name": text_name, "text": lines, "index": index})










else:


    # Load the entry from the data. Find the entry with the matching name.
    print("You already have this text.")



    print("Now attempting to grab the list entry corresponding to this title.")
    
    entry = next((item for item in data if item["name"] == text_name), None) 


    



    lines = entry["text"]

    index = entry["index"]



# Now: You have your variables. Start reading the text.


print(lines[index])
n = input()

while n != "q":

    index = index + 1
    print(lines[index])
    n = input()







# Lastly, rewrite the index to the data variable


i = next((ind for (ind, d) in enumerate(data) if d["name"] == text_name), None)

data[i]["index"] = index

with open("dr.dat", "w+") as f:
    json.dump(data, f)










