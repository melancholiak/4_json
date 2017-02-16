# Prettify JSON

The project itself consist of single script that takes path to json file and prints it to the terminal in human readable format,
instead of plain text (aka pretty printing).

# Quickstart

Example of script launch on Linux, Python 3.5:
Json file content: [{"1":["the","one"],"2":"to","4C":[{"4":"for","C":"see"},"forsee"],"4":"for","1+":"all"}]
  
```#!bash

$ python pprint_json.py data.json
# output:
[
  {
    '4C':[
      {
        '4':'for',
        'C':'see'
      },
      'forsee'
    ],
    '2':'to',
    '4':'for',
    '1':[
      'the',
      'one'
    ],
    '1+':'all'
  }
]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
