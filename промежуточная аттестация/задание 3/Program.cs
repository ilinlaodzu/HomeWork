//Задача 3: Задайте произвольный массив.
 //Выведете его элементы, начиная с конца. Использовать рекурсию, не использовать циклы.

Console.Write ("Введите количество элементов массива " );
int size = Convert.ToInt32(Console.ReadLine());
int[] array = new int[size];
Random m = new Random();

for (int i = 0; i < size; i++) 
{
    array[i] = new Random().Next(0,10);
    System.Console.Write(array[i] + " ");
}
 System.Console.Write ("\n");
void PrintArray (int[] array, int size,  int i)
{
  if (i == size) {
    return;
  }
   
  if (i < size) {
    PrintArray (array, size, i + 1);
    System.Console.Write(array[i] + " ");
  } 
}

PrintArray(array, array.Length, 0);

