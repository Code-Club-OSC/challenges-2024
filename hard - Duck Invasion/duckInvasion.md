# DUCK INVASION
Rubber ducks are secretly planning to take over the world and enslave human kind as workers in their mega cracker factory. This is a stealth operation. The ducks are distributed throughout the world, using their cuteness to gain people's trust. Once the number of ducks becomes strictly greater than the human population, commander duck will give the order to attack.

You like crackers so you decide to help. You are given the number of ducks already distributed, the number of additional ducks distributed each day, the number of duck casualties each day (sadly, some ducks are lost, burned, or squashed), and the human population size. Determine how many days the ducks will wait before attacking.

Input
Four integers, each on their own line, are

S, the number of ducks already distributed where S<P.
D, the number of additional ducks distributed each day.
C, the number of duck casualties each day where C<D.
P, the human population where P≥1.
It also holds that 0≤D,P,S<100,000. You do not need to error check for these conditions in your code. They will always be true. Quick and dirty code is encouraged :)

Output
Print a single integer representing the number of days the ducks will lay in wait before the attack.
Sample Input 1
0
2
0
10
Sample Output 1
5
 
Sample Input 2
3
6
2
10
Sample Output 2
1
