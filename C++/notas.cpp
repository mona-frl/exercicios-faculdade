#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
/*#include <stdio.h>
Obter notas
Calcular média
Verificar se o aluno foi reprovado ou não 
Se média > 7, aprovado senão reprovado
*/

int main(void) {
//declaração variaveis
float nota1, nota2, media;

//obter notas
  printf("Digite a primeira nota: ");
  scanf("%f", &nota1);

 printf("Digite a segunda nota: ");
  scanf("%f", &nota2);

// Calcular média
media= (nota1 + nota2)/2;

// Verificar se o aluno foi aprovado
if (media >= 7)
printf("Aprovado");
else
printf("Reprovado");

	return 0;
}
