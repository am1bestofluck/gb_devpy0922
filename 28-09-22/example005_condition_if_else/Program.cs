// // See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");
Console.Write("Kto ty?");
string username = Console.ReadLine();
string vip="ANTOHA";
string sayMyName="";
if (username.ToUpper()==vip){
    sayMyName="Привет заюша!";
}
else{
    sayMyName="Здрасте";
};
System.Console.WriteLine(sayMyName);