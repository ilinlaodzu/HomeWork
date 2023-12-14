// Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N. 
//Использовать рекурсию, не использовать циклы.
int ReadInt(string str)
{
    System.Console.Write(str);
    return Convert.ToInt32(Console.ReadLine());
}


void PrintNumbers (int A, int B)
{
  if (A == B) {
    System.Console.Write(A + " ");
    return;
  }
   
  if (A < B) {
    PrintNumbers (A, B - 1);
    System.Console.Write(B + " ");
  } else {
    PrintNumbers (B, A - 1);
    System.Console.Write(A + " ");
  }
}

int M= ReadInt("Введите значение больше нуля : ");
int N= ReadInt("Введите значение больше предыдущего : ");

PrintNumbers(M, N);