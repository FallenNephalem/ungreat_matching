# UNMATCH
Welcome to documentation of ungreat matching of strings module. Here i will tell you how to use it.


## ungreat_match(str1,str2,mkdefolt=0.7,mismatching_chars=5)
_A function, which ungreat matching your strings and return a list with result_
* `str1` and `str2` -- strings, which you are matching
* `mkdefolt` -- coefficient, which set value of equal characters. Can get value in the range of 0 to 1.
* `mismatching_chars` -- value of mismatching characters between `str1` and `str2`
This function return a list with result and status of work, like:
`
['python', 'True']
['mismatching skills', 'False', 2]
`
## example of usage
It is a little test of library, which i were using when testing my lib. If you want to test or pass different value to the function, you can open your terminal or command prompt at folder `path_to_your_virtual_environment/lib/site-packages/unmatch` and run it by writing `python test.py` or `python3 test.py` at command prompt, if you on Windows, or terminal, if you on Linux.
Code of `test.py`:
```
from ungreat_matching import ungreat_match, num_match_max, num_match_min


test_data = [['python','Python'],
['python','python3.7'],
['PYTHON','python3.7'],
['PYTHON','python3.7.3']]
for data in test_data:
    print(ungreat_match(data[0],data[1], mismatching_chars=5, mkdefolt=0.7))
```
Here i am showing, how it works.
(All text, what you put in function `ungreat_match` will convert to lower case and result of function will always give you a lower case result)

## What's new:
### 1.1.0:
* some changes in realization of library and optimization
* upgrade of documentation
You can see source code on [Github repository](https://github.com/FallenNephalem/ungreat_matching) of project.
