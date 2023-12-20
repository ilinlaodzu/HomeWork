// Задайте произвольную строку. Выясните, является ли она палиндромом.
string str = "Она не жена, но";
string clearStr = "";// переменная , которую определяе палиндром ли она
for (int i = 0; i<str.Length; i++)
{
     if (Char.IsLetterOrDigit(str[i])) //IsLetterOrDigit - буква или число
     {
        // clearStr += str[i].ToString().ToLower();//создала новую строку без лишних элементов пробелов и зяпятых онанеженано ToString().ToLower() -перевод в строку и нижний регистр
        clearStr += Char.ToUpper(str[i]);
        //clearStr = clearStr + Char.ToUpper(str[i]);
     }
}

// Console.WriteLine (clearStr);
int size = clearStr.Length;
int middle = size/2;
Boolean isPalindrom = true;
for (int i = 0; i < middle; i++)
{
    if (clearStr[i] != clearStr[size -i -1])
    {
    isPalindrom = false;
     Console.Write ("\nСтрока '" + str + "' не палиндром" );
     break;
    }

}
if (isPalindrom)
{
  Console.Write ("\nСтрока '" + str + "' палиндром" );  
}





