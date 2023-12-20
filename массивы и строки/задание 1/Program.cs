// Задайте двумерный массив символов (тип char [,]).
// Создать строку из символов этого массива.
char [] chars = {'a','b','c','d'};
string str = " ";
for ( int i=0; i<chars.Length; i++)
{
    str += chars [i];
}
System.Console.WriteLine (str);




//string str = new string (chars);