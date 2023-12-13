//Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.

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
int[,] mat = new int [9,15];

FillArray(mat);
Console.WriteLine("Исходный массив: ");
PrintArray(mat);

int temp;
int rowCount = mat.GetLength(0);
for (int y = 0; y<mat.GetLength(1); y++)
{
    temp = mat [0, y];
    mat [0,y] = mat [rowCount-1,y];
    mat [rowCount -1,y] = temp;
}
Console.WriteLine("Перевернутый  массив: ");
PrintArray(mat);