Problem Statement
The employee retention rate of XYZ company was very poor in the last year. It is found that the problem mainly lies in the employee appraisal system. This year new HR joined and introduced the following method-

Salary will be based on the performance rating of the employees i.e. higher rating will result higher hike in the salary. It is assumed that an employee is only aware of the salary hike and ratings of his colleagues sitting next left and right side of him.

The ratings of the employees are stored in an array arr[N] where N is the number of employees.

Write a program to calculate the minimum increase in remuneration so that everybody feels fair about it.



Example



Input: arr[] = {1, 3, 5, 4}

 Output: 1 2 3 1 // indicating salary hike

Input: arr[] = {5, 3, 4, 2, 1, 6}

 Output: 2 1 3 2 1 2

Explanation:  The 1st employee with lowest rating has the lowest hike of 1 unit. The next employee has better rating than him, so the next employee gets better hike of 2 unit. Third Employee has even better rating than the second employee. So he should have a hike of 3 unit. Now the fourth employee has a lower rating than the third, and as he can not contact the second one, his rating would be decreased to 1 as he would feel that the left neighbor employee had a better rating so he had a better hike. The fourth employee would remain happy.

Input Format
The first line of the input contains an positive integer n i.e. number of elements of the array

The second line contains array elements

Output Format
The hikes are positive integers only and the ratings are always greater than zero. Minimum salary hike is 1.

Constraints
Array of positive numbers (greater than zero) representing the hike

Time Limit
1s.
Each test case should pass in 1s.
Sample Input
5 
2 5 1 3 7
Sample Output
1 2 1 2 3