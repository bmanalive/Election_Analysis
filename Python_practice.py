#%% 
from typing import AbstractSet


print("Hello World")
# %%
one = 5+2*3
two = 8//5-3
three = 8+22*2-4
four = 16-3/2+7-1
five = 3**3%5
six = 5+9*3/2-4

print(one,two,three,four,five,six)
print(one)
print(two)
# %%
one = (5+2)*3
two = (8//5)-3
three = 8+(22*(2-4))
four = 16-3/(2+7)-1
five = 3**(3%5)
six = 5+(9*3/2-4)

print(one,two,three,four,five,six)
print(one)
print(two)
# %%
counties = ["Arapahoe","Denver","Jefferson"]
counties
# %%
counties[0]
print(counties[2])


# %%
print(counties[-1])

# %%
print(counties[-2])

# %%
len(counties)
# %%
counties[0:2]
# %%

counties[:2]

# %%
counties[1:]
# %%
counties[1:2]
# %%
counties[1:3]
# %%
counties.append('El Paso')
# %%
len(counties)
# %%
print(counties)
# %%
counties
# %%
counties.insert(2,"El Passo")
# %%
counties
# %%
counties.remove("El Paso")
# %%
counties
# %%
counties.pop(2)
# %%
counties
# %%
counties[2]="El Paso"
# %%
counties
# %%
counties[2]="Jefferson"
# %%
counties
# %%
counties[1]="El Paso"
counties
#%%
counties.pop(0)
counties
# %%
counties.append("Denver")
# %%
counties
# %%
counties.append("Arapahoe")
# %%
counties
# %%
counties_dict = {"Arapahoe":422829}
counties_dict



# %%
counties_dict["Arapahoe"]=422829
counties_dict
# %%
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438

# %%
len(counties_dict)
# %%
counties_dict.items()

# %%
counties_dict.keys()

# %%
counties_dict.values()
# %%
counties_dict.get("Denver")

# %%
counties_dict[('Arapahoe')]
# %%
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data
# %%
voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
voting_data
# %%
voting_data.remove({"county":"Arapahoe","registered_voters":422829})
voting_data
# %%
# %%
# %%
# %%

voting_data.remove({"county":"Denver","registered_voters":463353})
voting_data.insert(2,{"county":"Denver","registered_voters":463353})
voting_data
# %%
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data
# %%
if counties[1]=='Denver':
    print(Counties[1])
# %%

temperature = int(input("What is the temperature outside? "))
if temperature> 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
# %%
counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El paso is not the list of counties.")
       

# %%
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
# %%
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
# %%
for county in counties:
    print(county)
# %%
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
# %%
for num in range(5):
    print(num)
# %%
for i in range(len(counties)):
    print(counties)
# %%
for i in range(len(counties)):
    print(counties[i])
# %%
for i in len(counties_tuple):
      print(counties_tuple[i])
# %%
for county in counties_tuple:
      print(county)


# %%
for county in counties_dict:
    print(county)
# %%
for county in counties_dict.keys():
    print(county)
# %%
counties = counties_dict

for county in counties.keys():
    print(county)
# %%
for i in counties_dict.values():
    print(i)
# %%
for county in counties_dict:
    print(counties_dict[county])
# %%
for county in counties_dict:
    print(counties_dict.get(county))
# %%
for county, voters in counties_dict.items():
    print(county, voters)
# %%
for key, value in counties_dict.items():
    print(county, voters)
# %%
for county, voters in counties_dict.items():
    print(county + " county has "+ str(voters)+" registered voters.")
# %%
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
# %%
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# %%
for county_dict in voting_data:
    print(county_dict['county'])
# %%
for county_dict in voting_data:
    print(county_dict['registered_voters'])
# %%
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# %%
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
# %%
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
# %%
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
# %%
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# %%
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

# %%
voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
 for voting_data, registered_voters in voting_data.items():
     for keys, values in county_dict.items():
         print(f'{key} county has {value:,} registered voters. ')

# %%
dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

# %%
dir(str)
# %%
dir(int)
# %%
dir(float)
# %%
