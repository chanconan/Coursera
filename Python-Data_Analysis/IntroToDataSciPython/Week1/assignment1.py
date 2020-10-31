import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    result = re.findall('[A-Z]\w+', simple_string)
    return result

assert len(names()) == 4, "There are 4 names"

def grades():
    with open ("/Users/conanchan/Documents/Coursera/Python-Data_Analysis/IntroToDataSciPython/Week1/assets.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    result = re.findall('\w+ \w+(?=: B)', grades)
    return result
print(len(grades()))
assert len(grades()) == 16

def logs():
    with open("/Users/conanchan/Documents/Coursera/Python-Data_Analysis/IntroToDataSciPython/Week1/logdata.txt", "r") as file:
        logdata = file.read()
    result = []
    # YOUR CODE HERE
    regex = "(?P<host>(?:\d{1,3}\.){3}\d{1,3}) - (?P<user_name>[\w]+|-) \[(?P<time>\d+/\w+/([\d]+:){3}\d+ -\d+)\] \"(?P<request>\w+ (/[\w\-\%\+]+)+ \w+/\d.\d)"
    for item in re.finditer(regex, logdata):
        result.append(item.groupdict())
    return result

assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
