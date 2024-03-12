A house has N stories, where N is a whole number.

Each story is made out of struts, which may be supported by platforms.

The top story has 2 struts and 1 platform.
The second-to-top story has 4 struts and 2 platforms.
The third-to-top story has 6 struts and 3 platforms.
In general, each story has 2 more struts and 1 more platform than the story above it.

Note that the bottom story does not have a platform, because the table is already supporting it.

How many cards are needed to build a house with N stories?

Input
Input is an integer, 0<N≤10,000, which is the number of stories.

Output
Output an integer, K, the number of cards needed to build a house with N stories.

Example
Example house of cards with 4 stories

This house has 4 stories. There are 2 + 4 + 6 + 8 = 20 struts and 1 + 2 + 3 = 6 platforms in this house.

This adds up to 20 + 6 = 26 cards.

Sample Input 1
4
Sample Output 1
26