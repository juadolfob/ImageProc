#include <stdlib.h>
#include <stdio.h>

/*
  Funciones:
  float **Imagen = pgmread("imagen.pgm", &Largo, &Alto);
  int pgmwrite(float **Imagen, "archivo.pgm", Largo, Alto);
  float **Matriz(int, int, int);
  float  *Vector(int, int);
*/
int Largo, Alto;

float *Vector();

void **Matriz(int, int, int);

char **pgmread();

int pgmwrite();

int getint(FILE *);

void **Matriz(int rows, int columns, int elem_size) {/*int rows;       number of rows */
/*int columns;    number of columns */
/* int elem_size; element size */
    int row;
    void **array = (void **) malloc(rows * sizeof(void *));
    if (array == NULL)
        printf("Error al asignar lineas a la matriz\n"), exit(0);

    for (row = 0; row < rows; row++) {
        array[row] = (void *) calloc(columns, elem_size);
        if (array == NULL)
            printf("Error al asignar columnas a la matriz\n"), exit(0);
    }

    return array;
}

float *Vector(int i0, int i1) {
    float *v;
    if ((v = (float *) calloc(i1 - i0 + 1, sizeof(float))) == NULL)
        printf("Error al asignar memoria al vector\n");
    return v - i0;
}

int getint(FILE *fd) {
    int c, i;
    char dummy[10000];

    c = getc(fd);
    while (1) /* find next integer */
    {
        if (c == '#')    /* Descartar los comentarios */
            fgets(dummy, 9000, fd);
        if (c == EOF) {
            return 0;
        }
        if (c >= '0' && c <= '9')
            break;   /* found what we were looking for */
        c = getc(fd);
    }

    /* we're at the start of a number, continue until we hit a non-number */
    i = 0;
    while (1) {
        i = (i * 10) + (c - '0');
        c = getc(fd);
        if (c == EOF) return (i);
        if (c < '0' || c > '9') break;
    }

    return (i);
}

void Free(void **array, int rows)
/*void **array;   the two-dimensional array
int rows;      /* number of rows */
{
    int row;
    for (row = 0; row < rows; row++) {
        free(array[row]);
    }
}

char **pgmread(char *filename, int *x_size, int *y_size) {
    FILE *fd;
    char header[100];
    int tmp;
    int x, y, Contador = 0;
    char **Imagen;

    if ((fd = fopen(filename, "rb")) == NULL) {
        printf("No puedo abrir %s para lectura!\n", filename);
        exit(0);
    }

    /* Leyendo el encabezado */
    header[0] = fgetc(fd);
    header[1] = fgetc(fd);
    if (!(header[0] == 'P' && header[1] == '5')) {
        printf("Error al leer el archivo\nLa imagen %s no es un PGM!\n", filename);
        fclose(fd);
        exit(0);
    }

    *x_size = getint(fd);
    *y_size = getint(fd);
    tmp = getint(fd);

    Imagen = (char **) Matriz(*x_size, *y_size, sizeof(char));

    /* Toma la imagen del archivo */
    for (y = 0; y < *y_size; y++)
        for (x = 0; x < *x_size; x++, Contador++)
            Imagen[x][y] = (char) fgetc(fd);

    /* Verifico que se leyeron todos los bytes */
    if (Contador != (*x_size * *y_size)) {
        printf("Archivo con longitud incorrecta!\n");
        return Imagen;
    }

    fclose(fd);
    printf("Cargando imagen %s\n", filename);
    return Imagen;
}

int pgmwrite(char **Imagen, char *filename, int Largo, int Alto) {
    FILE *Out;
    int x, y, Contador = 0;

    if ((Out = fopen(filename, "wb")) == NULL) {
        printf("No puedo escribir la imagen!\n");
        return 0;
    }

    /* Ponemos el encabezado de los PGM */
    fprintf(Out, "P5\n");
    fprintf(Out, "%d %d\n", Largo, Alto);
    fprintf(Out, "255\n");

    /* Vacio la imagen al archivo */
    for (y = 0; y < Alto; y++)
        for (x = 0; x < Largo; x++, Contador++)
            fputc(Imagen[x][y], Out);

    /* Verifico que se escriban todos los bytes */
    if (Contador != (Largo * Alto)) {
        printf("Archivo con longitud incorrecta!\n");
        return 0;
    }

    fclose(Out);

    printf("\nSalvando %s PGM de %ix%i\n", filename, Largo, Alto);
    return 1;
}
