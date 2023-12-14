// Задача 2: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
//m = 2, n = 3 -> A(m,n) = 9
//m = 3, n = 2 -> A(m,n) = 29

Console.Write("Введите число M: ");
int m = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите число N: ");
int n = Convert.ToInt32(Console.ReadLine());


int Ak (int m, int n)
{
    if (m == 0) 
    {
        return n+1;
    }
    if (m>0 && n==0)
    {
        return Ak (m-1, 1);
    }
 
     return Ak (m- 1, Ak (m, n-1) );

}

Console.WriteLine ("Значение функции Аккермана A (" + m + " , " + n + " ) = " + Ak (m , n));


