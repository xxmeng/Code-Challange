# Code-Challange

The Task
An automated traffic counter sits by a road and counts the number of cars that go
past. Every half-hour the counter outputs the number of cars seen and resets the counter
to zero. You are part of a development team that has been asked to implement a system to
manage this data - the first task required is as follows:
Write a program that reads a file, where each line contains a timestamp (in yyyy-mmddThh:mm:ss format, i.e. ISO 8601) for the beginning of a half-hour and the number of
cars seen that half hour. An example file is included on page 2. You can assume clean
input, as these files are machine-generated.

## The program should output:
• The number of cars seen in total
• A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the
• number of cars seen on that day (eg. 2016-11-23 289) for all days listed in the input file.
• The top 3 half hours with most cars, in the same format as the input file
• The 1.5 hour period with least cars (i.e. 3 contiguous half hour records)


## Constraints
• The program can be written in Java, Scala or Python, and with any libraries you are
familiar with. You are encouraged to use modern versions of each language and make
use of their features.
• The program must be accompanied with reasonable levels of unit tests.
• The solution should be developed to professional standards, the code may be used and
extended by your teammates.
• The solution should be deliverable within a couple of hours - please do not spend
excessive amounts of time on this.
• Avoid over-engineering.

## Assessment
Your submission will be assessed on the following:
• Correctness of solution
• Readability and fluency of your code (including tests)
• Effectiveness of your tests

## Sample Input
2021-12-01T05:00:00 5
2021-12-01T05:30:00 12
2021-12-01T06:00:00 14
2021-12-01T06:30:00 15
2021-12-01T07:00:00 25
2021-12-01T07:30:00 46
2021-12-01T08:00:00 42
2021-12-01T15:00:00 9
2021-12-01T15:30:00 11
2021-12-01T23:30:00 0
2021-12-05T09:30:00 18
2021-12-05T10:30:00 15
2021-12-05T11:30:00 7
2021-12-05T12:30:00 6
2021-12-05T13:30:00 9
2021-12-05T14:30:00 11
2021-12-05T15:30:00 15
2021-12-08T18:00:00 33
2021-12-08T19:00:00 28
2021-12-08T20:00:00 25
2021-12-08T21:00:00 21
2021-12-08T22:00:00 16
2021-12-08T23:00:00 11
2021-12-09T00:00:00 4
