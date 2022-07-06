# print total number of country details
# print languages of ukrane
# print currency of china
# print population of india
# print nigehbouring countries of australia
# import json
# with open("countries.json") as f:
#     data=json.load(f)
# print(len(data))
# india_detail=[for country in data if country["name"]=="India"]
# print(india_detail)
import json

with open("countries.json", encoding="utf") as f:
    data = json.load(f)

# print total number of country details
print(len(data))

# print languages of ukraine
ukrn_lan = [country["languages"] for country in data if country["name"] == "Ukraine"]
print(ukrn_lan)
for lan in ukrn_lan[0]:
    print(lan["name"])

# print currency of china
cur_china = [country["currencies"] for country in data if country["name"] == "China"]
print(cur_china)

# print currency name of palestine
cur_pale = [country["currencies"] for country in data if country["name"].startswith("Palestine")]
print(cur_pale)

# #print population of india
# pop_ind=[country["population"] for country in data if country["name"]=="India"]
# print(pop_ind)


# print neighbouring countries of australia
# astr=[country["borders"] for country in data if country["name"]=="Australia" ]
# print(astr)

# print(language by country)
currency_detail = [country["currencies"] for country in data if country["name"].lower().startswith("sri")]
currency_name = [details.get("name") for details in currency_detail[0]]


# print currency name
def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]


aust_data = get_country_data("austria")
print(aust_data[0].get("borders"))

# india_data=get_country_data("india")
# print(india_data[0].get("borders"))

country_data = get_country_data("india")
country_borders = country_data[0].get("borders")
sharing_borders = [country.get("name") for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)

# print max population of india
pop_country = max(data, key=lambda d: d.get("population"))
print(pop_country["name"])

# print min population of india
pop_country = min(data, key=lambda d: d.get("population"))
print(pop_country["name"])
