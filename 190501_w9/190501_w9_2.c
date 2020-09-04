#include<stdio.h>
#include<stdlib.h>

int main()
{
   int a, b, c, d;

   printf("A + B - C = ?\n");

   printf("Input A: ");
   scanf("%d", &a);

   printf("Input B: ");
   scanf("%d", &b);

   printf("Input C: ");
   scanf("%d", &c);

   d = a + b - c;

   printf("%d + %d - %d = %d\n", a, b, c, d);

   system("PAUSE");
   return 0;
}
