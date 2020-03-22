import json

json_sample = {
    "data": {
        "numbers": [1, 2, 3, 4, 5],
        "contact": {
            "email": "abc@abc.com",
            "number": "8585858585",
            "url": "www.abc.com"
        },
        "bio": "new data",
        "information": {
            "year": "2019",
            "education": [
                {
                    "start_year": "2006",
                    "end_year": "2011",
                },
                {
                    "start_year": "2011",
                    "end_year": "2015",
                },
                {
                    "start_year": "2017",
                    "end_year": "2019",
                }
            ],
            "education_2": [
                {
                    "start_year": "2006",
                    "end_year": "2011",
                },
                {
                    "start_year": "2011",
                    "end_year": "2015",
                },
                {
                    "start_year": "2017",
                    "end_year": "2019",
                }
            ]
        }
    }
}

to_update = {
    "data": {
        "numbers": [4, 5, 6, 7, 8],
        "contact": {
            "email": "abcd@abcd.com",
            "email_2": "abcde@abcde.com",
            "number": "9696969696",
            "number_2": "4949494949"
        },
        "information": {
            "year": "2020",
            "education_2": [
                {
                    "start_year": "2017",
                    "end_year": "2020",
                }
            ]
        }
    }
}


def update(data, other):
    for key, value in other.items():
        if key in data.keys():
            if isinstance(data[key], dict):
                data[key] = update(data[key], value)
            elif isinstance(data[key], list) and isinstance(value, list):
                data[key].extend(value)
                data[key] = [json.dumps(i) if isinstance(i, dict) else i for i in data[key]]
                data[key] = list(set(data[key]))
                for i, j in enumerate(data[key]):
                    try:
                        data[key][i] = json.loads(j)
                    except:
                        pass
            else:
                data[key] = value
        else:
            data[key] = value
    return data


print(update(data=json_sample, other=to_update))
