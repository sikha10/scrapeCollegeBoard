import json

f = open('allColleges.json', 'r')
all_colleges = f.readline()
all_colleges_json = json.loads(all_colleges)

# print(all_colleges_json)

private_colleges = []
private_colleges_under_10 = []
private_colleges_none = []

for college in all_colleges_json:
    if college['info'].__contains__("Private") or college['info'].__contains__("International"):
        private_colleges.append(college)


for private_college in private_colleges:
    if private_college['average cost per year after aid'] == 'None':
        private_colleges_none.append(private_college)
    if len(private_college['average cost per year after aid']) == 4 and private_college['average cost per year after aid'] != 'None':
        avg_price = int(private_college['average cost per year after aid'][1:3])
    if len(private_college['average cost per year after aid']) == 3:
        avg_price = int(private_college['average cost per year after aid'][1])
    
    # print(avg_price)

    if avg_price <= 15 and avg_price > 10:
        private_colleges_under_10.append(private_college)

print(private_colleges_under_10)
print()
print(private_colleges_none)

