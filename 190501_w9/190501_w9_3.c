#include <stdio.h>
#include <stdlib.h>

int main(){

    int run = 1;
    while (run == 1){
        int n,sqr;

        printf("=========================\n");
        printf("Please input a number: ");
        scanf("%d",&n);
        sqr = sqrt(n);

        if (n%sqr != 0)
            printf("\n%d is not a square number.\n",n);
        else
            printf("\n%d is a square number of %d\n", n, sqr);

        printf("\nContinue? [yes<1>, no<2>]\n");
        scanf("%d",&run);

    }
    printf("=========================\n");
    printf("Good bye!\n");

    system("PAUSE");
    return 0;
}
