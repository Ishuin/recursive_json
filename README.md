# Update Recursive JSON

## Getting Started

### Input data

Let's say we initially have this JSON data that needs to be updated.
```text
data_a = {
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
```

And we have this data that we need to add to the existing JSON data (dictionary type)

```buildoutcfg
data_b = {
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
```
---
### Output data

 We will use the program as `data_c = update(data=data_a, other=data_b)` where `data_c` will be returned as the data below
 
 ```buildoutcfg
data_c = {
    'data': {
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8], 
        'contact': {
            'email': 'abcd@abcd.com', 
            'number': '9696969696', 
            'url': 'www.abc.com', 
            'email_2': 'abcde@abcde.com', 
            'number_2': '4949494949'
        },
        'bio': 'new data', 
        'information': {
            'year': '2020', 
            'education': [
                {
                    'start_year': '2006',
                    'end_year': '2011'
                },
                {
                    'start_year': '2011',
                    'end_year': '2015'
                }, 
                {
                    'start_year': '2017', 
                    'end_year': '2019'
                }
            ], 
            'education_2': [
                {
                    'start_year': '2011', 
                    'end_year': '2015'
                }, 
                {
                    'start_year': '2017', 
                    'end_year': '2020'
                }, 
                {
                    'start_year': '2006', 
                    'end_year': '2011'
                }, 
                {
                    'start_year': '2017', 
                    'end_year': '2019'
                }
            ]
        }
    }
}
```

**Note:** 
1. Data samples taken here are added by my individual understanding, therefore, the code is designed considering the input provided. If someone could find sample data that could break the code, please update me with the code sample and I will do my best to fix the code according to that data also.
2. Pull requests are also welcome.
