 comparing run time for array.concat VS array.forEach when building a new array.
 
 Is it overcomplicated? yes
 
 is it accurate? I sure hope so

|

|
### Trail Results for 5 Rounds, 10000000 array length
|index  | forEachTime | concatTime|
| :--:  | :--:        |   :---:   |
| 0     |    330      |    34     |
| 1     |    247      |    34     |
| 2     |    396      |    35     |
| 3     |    283      |    34     |
| 4     |    389      |    37     |

### Average Times

forEach : 329

concat  : 34.8

speed up: 9.454022988505749

