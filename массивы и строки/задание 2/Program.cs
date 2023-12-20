//Задайте строку, содержащую латинские буквы в обоих регистрах.
// Сформируйте строку, в которой все заглавные буквы заменены на строчные. 


string lat = "abdjkgjgGKKHnmvvn";
// string Lower_lat = "";// нижний регистр lat
// foreach  (char a in lat) //для каждого элемента строки lat 
// {
//     Lower_lat += a.ToString().ToLower();
// }
// System.Console.WriteLine (Lower_lat);
System.Console.WriteLine (lat.ToLower());
