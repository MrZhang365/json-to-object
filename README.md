# json-to-object
It can convert JSON string to object

## How to use it
```python
import json_to_object
import json
test_dict = {'name':'Mr_Zhang','age':14,'hobbies':['programming','play chess'],'not_a_bot':True}
json_text = json.dumps(test_dict) #Generate JSON data for testing
user = json_to_object.loads(json_text)
print('''Name: {}
Age: {}
Hobbies: {}
Not a robot: {}'''.format(user.name,str(user.age),str(user.hobbies),str(user.not_a_bot)))
```
