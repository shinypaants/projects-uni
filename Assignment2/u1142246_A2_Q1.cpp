#include <iostream>
#include <string>
#include <vector>
#include <istream>
#include <map>

using namespace std;

string staffName;
int staffProf;
string staffJob[4] = {"Receptionist", "Administrator", "Nurse", "Doctor"};
void printEntry(string name, int staffProf)
{
    if (staffProf == 1)
    {
        cout << "Staff " << name << " is a " << staffJob[0] << endl;
    }
    else if (staffProf == 2)
    {
        cout << "Staff " << name << " is an " << staffJob[1] << endl;
    }
    else if (staffProf == 3)
    {
        cout << "Staff " << name << " is a " << staffJob[2] << endl;
    }
    else
    {
        cout << "Staff " << name << " is a " << staffJob[3] << endl;
    }
}

int main()
{
    do // did a do-while loop as i wanted the program to "do this and that" while !done but couldn't get it to work so left as (true) with a break in if true.
    {
        cout << "Please enter a staff name('done' to leave the program): " << endl;
        getline(cin, staffName);
        if (staffName == "done")
        {
            break;
        }
        cout << "Please enter the profession of " << staffName << endl;
        cin >> staffProf;
        if (cin.fail())
        {
            cout << "Wrong Entry!" << endl;
            cin.clear();
            cin.ignore(100, '\n');
        }
        else
        {
            printEntry(staffName, staffProf);
            cin.clear();
            cin.ignore(100, '\n');
        }

    } while (true);
    return 0;
}