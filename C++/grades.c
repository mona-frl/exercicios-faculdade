#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {

/*
Obtain grades
Calculate grades
Verify if the student is approved or reproved 
If the the average grade is > 7 = approved if < 7 = reproved 
*/

//Variables Declaration
float grade1, grade2, avg;

//Obtaining the grades
  printf("Enter the first grade: ");
  scanf("%f", &grade1);

 printf("Enter the second grade: ");
  scanf("%f", &grade2);

// Calculating the average grade
avg= (grade1 + grade2)/2;

// Verifying the avg grade
if(avg >= 7)
printf("The student has been approved.");
else
printf("The student has been reproved.");

 return 0;

}
