#include <stdio.h>

int main(int argc, char *argv[]){
    char buf[256];

    gets(buf);
    printf("%s\n", buf);
}

