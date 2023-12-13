//Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, 
//и возвращает значение этого элемента или же указание, что такого элемента нет.


void FillArray(int[,]mat)
{
    for (int i = 0; i<mat.GetLength(0); i++)
    {
        for (int j = 0; j<mat.GetLength(1); j++)
        {
            mat[i,j] = new Random().Next(1,99);
        }
    }

}
void PrintArray(int[,] array)
{
    for (int i = 0; i<array.GetLength(0); i++)
    {
        for (int j = 0; j<array.GetLength(1); j++)
        {
            Console.Write($"{array [i,j]} ");
        }
        Console.WriteLine(); 
    }

}

int CheckAndGetIndex(string text)
{   
    if (text == null)
    {
     return -1;
    }
    int number;
    if (int.TryParse(text, out number))
    {
        if (number < 0 )
        {
          return -1;
        }
      return number;
    } else 
    {
      return -1;
    }
}
int[,] mat = new int [6,5];
//for (int i =0; int<mat.GetLength(0); int++)
FillArray(mat);
PrintArray(mat);

// Console.Write ("Введите индекс строки  " );//x 
// int x = CheckAndGetIndex(Console.ReadLine());
// if (x==-1) 
// {
//    Console.Write ("Введенный индекс  строки не число");
//    return;
// }
// else if (x==-2)
// {
//    Console.Write ("Введенный индекс  строки отрицательное  число");
//    return;
// }
int y;
int x;
while (true) {
    Console.WriteLine ("Введите индекс строки  " );//x 
     x = CheckAndGetIndex(Console.ReadLine());
  if (x==-1) 
  {
     Console.WriteLine ("Введенный индекс  строки не коррректное  число");
     continue;
  }
  Console.WriteLine ("Индекс строки  " + x );
   break;
}

while (true) {
    Console.WriteLine ("Введите индекс столбца  " );//y 
     y = CheckAndGetIndex(Console.ReadLine());
  if (y==-1) 
  {
     Console.WriteLine ("Введенный индекс  столбца не коррректное  число");
     continue;
  }
  Console.WriteLine ("Индекс столбца  " + y );
   break;
}

if (x<mat.GetLength(0) && y<mat.GetLength(1))
{
    Console.WriteLine ("Значение элемента " +  mat [x,y]);
}
else
{
    Console.WriteLine ("Такого элемента нет");
}
