import json
class JSON_Object:
    def __init__(self) -> None:
        pass
def loads(text) -> JSON_Object:
    '''
        text: 一个JSON字符串
    '''
    json_dict = json.loads(text)
    new_object = JSON_Object()
    for i in json_dict:
        if type(json_dict[i]) == str:
            exec('new_object.{} = \'{}\''.format(i,json_dict[i]))
        else:
            exec('new_object.{} = {}'.format(i,json_dict[i]))
    return new_object