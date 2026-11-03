#include <stdio.h>

int main(int argc, char *argv[]){
        FILE *file = fopen(argv[1], "r");
        int ch;
        int new_ch;
        int i = 0;
        while((ch = fgetc(file)) != EOF){
                new_ch = ch - i;
                printf("%c", new_ch);
                i +=1;
        }
        fclose(file);
        return 0;
}