#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("<<< Interview for Travel Plan >>>\n");

    printf("Input your name: ");
    char name[20];
    scanf("%s",&name);

    printf("Gender: ");
    char gender[20];
    scanf("%s",&gender);

    printf("Date of Birth: ");
    int bday;
    scanf("%d",&bday);

    printf("Destination: ");
    char dest[20];
    scanf("%s",&dest);

    printf("Trip: ");
    int trip;
    scanf("%d",&trip);

    printf("=========================\n");
    printf("NAME: %s\n",name);
    printf("GENDER: %s\n",gender);
    printf("DAY OF BIRTH: %d\n",bday);
    printf("DESTINATION: %s\n",dest);
    printf("PERIOD OF TRIP: %d\n",trip);
    printf("=========================\n");

    system("PAUSE");
    return 0;

}
