# Competition-Results

This python 3 script parses competition results from a results text file and outputs each line to a file from lowest placing to highest. This file can be read by other programs such as OBS to show the current competitor. 

Currently this script requires the python module colorama to run, which can be installed using 'pip install colorama'

In order to use this script, the results file must be formatted from 1st place to last place, with each place taking up a single line. To account for disqualified runs, *there must be an empty line separating the accepted and the disqualified results.* After this line, each disqualified entry should be on a single line. The first empty line is used as the DQ marker so every result after that point will be seen as a disqualified entry.

If there are no disqualified runs, the results file should end with two empty lines.

Example results format with DQ's:

```
1. winner
second place
3rd place
(empty line)
DQ 1
#2 DQ
```
Example results format without DQ's:
```
1. winner
second place
#3 player
(empty line)
(empty line)
```
