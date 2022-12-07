# The PA Directory Search Engine

## What to write here
You should present the following complexity analysis in this report:

+ Big-O complexity of the indexing operation.
+ Big-O complexity of a search operation (given that indexing has been done already).
+ Big-O complexity of a search operation if it were implemented in a brute force fashion (that is, no indexing performed, all search queries go through the entire text of all files every time).

You should be very clear about what you mean by n when presenting your Big-O complexity analysis.

## The Report
The indexing operation has a complexity of O(n^2) where n represents each word of each line of the file that is being indexed.

The search operation after indexing has a complexity of O(n) where n represents the number of words in the forward index of a file. This is quicker since the forward index already contains each word that exists in each file, reducing the O complexity so that the relationship between a file and the words in it does not have to be established and the words can just be looped through.

The Big O complexity of a search operation without indexing depends on how it is implemented. It would be O(n^3) as for every search it must be checked in a query encompassing each file, each line in that file and each word in that line.