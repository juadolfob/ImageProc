/*de compilaci�n: cc negativo.c pgm.c -o negativo

   Ejemplo del uso de:

   pgmread
   pgmwrite

   Las matrices que contienen a las im�genes son declaradas como uchar **

   % % % % % % % %

   Ejemplo 1:

   char **Original = (char **)pgmread(argv[1], &Largo, &Alto);
   La imagen PGM se lee de la l�nea de comando (argv[1]). La funci�n
   pgmread regresa tres valores:

   1. la imagen le�da       (Original)
   2. el largo de la imagen (Largo)
   3. el alto de la imagen  (Alto)

   % % % % % % % %

   Ejemplo 2:

   pgmwrite(Salida, "negativo.pgm", Largo, Alto);
   La imagen Salida es escrita al disco con el nombre de negativo.pgm, la
   imagen resulta en formato PGM. La imagen se escribe desde el inicio (0,0)
   hasta (Largo, Alto).
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "pgm.c"


/* Variables globales. Para que pasarlas
de funci�n a funci�n! */

/* * * * * Obtiene el negativo de una imagen * * * * */

int pgm127_255(int i) {
    return (i + 255) % 255;
}
int pgm255_127(int i) {
    if(i>127) {
        return i - 255;
    }else{
        return i;
    }
}
void Identidad(char **Original, char **Salida) {
    int x, y;

    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            Salida[x][y] = Original[x][y];
}
void Negativo(char **Original, char **Salida) {
    int x, y;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            Salida[x][y] = 255 - Original[x][y];
}
void Umbral(char **Original, char **Salida,int p) {
    int x, y;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            if(Original[x][y] <= p){
                Salida[x][y] = 0;
            }else{
                Salida[x][y] = 255;
            };
}
void Intervalo_Umbral_Binario(char **Original, char **Salida, int p1,int p2) {
    int x, y;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            if(Original[x][y] <= p1 || Original[x][y] >= p2){
                Salida[x][y] = 255;
            }else{
                Salida[x][y] = 0;
            };
}
void Intervalo_Umbral_Binario_Invertido(char **Original, char **Salida,int p1,int p2) {
    int x, y;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            if(Original[x][y] <= p1 || Original[x][y] >= p2){
                Salida[x][y] = 0;
            }else{
                Salida[x][y] = 255;
            };
}
void Umbral_Escala_Grises(char **Original, char **Salida,int p1, int p2) {
    int x, y;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            if(Original[x][y] <= p1 || Original[x][y] >= p2){
                Salida[x][y] = 255;
            }else{
                Salida[x][y] = Original[x][y];
            };
}
void Umbral_Escala_Grises_Invertido(char **Original, char **Salida,int p1,int p2) {
    int x, y;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            if(Original[x][y] <= p1 || Original[x][y] >= p2){
                Salida[x][y] = 255;
            }else{
                Salida[x][y] = 255-Original[x][y];
            };
}
void Extension(char **Original, char **Salida,int p1,int p2) {
    int x, y;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++)
            if(Original[x][y] <= p1 || Original[x][y] >= p2){
                Salida[x][y] = 0;
            }else{
                Salida[x][y] = (Original[x][y]-p1)*(255/(p2-p1));
            };
}




void Reduccion_Nivel_Gris(char **Original, char **Salida,int *q,int qn) {
    int x, y;
    printf("%d",qn);
    bool found_q=false;
    for (x = 0; x < Largo; x++)
        for (y = 0; y < Alto; y++){
            found_q=false;
            int original=pgm127_255(Original[x][y]);

            if(original<= q[0]){
                Salida[x][y] = 0;
                continue;
            }
            for(int i=1;i<=qn;i++){
                if(original> q[i-1] && original<= *(q+i)){
                    Salida[x][y] = pgm255_127(*(q+i-1));
                    found_q=true;
                    break;
                }
            }

            if(found_q){
                continue;
            }
            Salida[x][y] = pgm255_127(*(q+qn));
        }

}

/* * * * *          * * * * *          * * * * *          * * * * */

int main(int argc, char *argv[]) {
    char **Original = (char **) pgmread(argv[1], &Largo, &Alto);
    char **Salida = (char **) Matriz(Largo, Alto, sizeof(char));
    Identidad(Original, Salida);
    pgmwrite(Salida, "Identidad.pgm", Largo, Alto);
    Negativo(Original, Salida);
    pgmwrite(Salida, "Negativo.pgm", Largo, Alto);
    Umbral(Original, Salida,75);
    pgmwrite(Salida, "Umbral.pgm", Largo, Alto);
    Intervalo_Umbral_Binario(Original, Salida,50,175);
    pgmwrite(Salida, "Intervalo_Umbral_Binario.pgm", Largo, Alto);
    Intervalo_Umbral_Binario_Invertido(Original, Salida,50,175);
    pgmwrite(Salida, "Intervalo_Umbral_Binario_Invertido.pgm", Largo, Alto);
    Umbral_Escala_Grises(Original, Salida,10,120);
    pgmwrite(Salida, "Umbral_Escala_Grises.pgm", Largo, Alto);
    Umbral_Escala_Grises_Invertido(Original, Salida,10,120);
    pgmwrite(Salida, "Umbral_Escala_Grises_Invertido.pgm", Largo, Alto);
    Extension(Original, Salida,75,175);
    pgmwrite(Salida, "Extension.pgm", Largo, Alto);
    int a[]={75,100,170,210,230};
    Reduccion_Nivel_Gris(Original, Salida,a,sizeof(a)/sizeof(a[0]));
    pgmwrite(Salida, "Reduccion_Nivel_Gris.pgm", Largo, Alto);

}
