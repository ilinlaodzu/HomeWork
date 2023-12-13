//Задайте прямоугольный двумерный массив. 
//Напишите программу, которая будет находить строку с наименьшей суммой элементов.
void FillArray(int[,]mat)
{
    for (int i = 0; i<mat.GetLength(0); i++)
    {
        for (int j = 0; j<mat.GetLength(1); j++)
        {
            mat[i,j] = new Random().Next(1,10);
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
int[,] mat = new int [7,9];

FillArray(mat);
Console.WriteLine("Исходный массив: ");
PrintArray(mat);

int minSum =0;
int xMin = 1;
for (int x = 0; x< mat.GetLength(0); x++)
{
   int sum=0;
   for (int y = 0; y< mat.GetLength(1); y++)
   {
    sum +=mat [x,y];
   }
   //Console.WriteLine("Сумма элементов строки с индексом " + x + " равна " + sum);
   if (x==0)
   {
      minSum = sum;
   }
   else if (sum < minSum)
   {
    minSum=sum;
    xMin = x+1;
   }
}
Console.WriteLine("Cтрока с наименьшей суммой элементов равна " + xMin);