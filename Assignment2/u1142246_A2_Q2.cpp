#include <iostream>
#include <string>
#include <vector>
#include <istream>
#include <map>
#include <cstdio>

using namespace std;

// finished the use of struct and runs perfect without displaying the array
//ive commented the lines where you can comment out to see the result of using struct
// i've left working to show what i would do if it worked - feel so close to it but needed more time
struct staffStruct
{
    string staffName;
    int staffProf;
    string staffJob[4] = {"Receptionist", "Administrator", "Nurse", "Doctor"};
};

void printEntry(staffStruct staffTWB)
{
    if (staffTWB.staffProf == 1)
    {
        cout << "Staff " << staffTWB.staffName << " is a " << staffTWB.staffJob[0] << endl;
    }
    else if (staffTWB.staffProf == 2)
    {
        cout << "Staff " << staffTWB.staffName << " is an " << staffTWB.staffJob[1] << endl;
    }
    else if (staffTWB.staffProf == 3)
    {
        cout << "Staff " << staffTWB.staffName << " is a " << staffTWB.staffJob[2] << endl;
    }
    else
    {
        cout << "Staff " << staffTWB.staffName << " is a " << staffTWB.staffJob[3] << endl;
    }
}

// I think I needed more time on this part as question 1 was a bit hard to figure out
// This is what i could manage to do with the set time.
//delete this if you want to show structs working
//void printArray(staffStruct[], int counter)
//{
//    cout << "**********List of staffs******" << endl;
//    cout << staffName[counter] << endl;
//}

int main()
{
    // staffStruct staffTWB[50];
    staffStruct staffTWB;
    do
    {
        //for (int i = 0; i < 50; i++)
        //{
        cout << "Please enter a staff name('done' to leave the program): " << endl;
        // i would put an [i] infront of the staffTWB[i].
        getline(cin, staffTWB.staffName);
        if (staffTWB.staffName == "done")
        {
            //printArray(staffTWB, i);
            break;
        }
        cout << "Please enter the profession of " << staffTWB.staffName << endl;
        cin >> staffTWB.staffProf;
        if (cin.fail())
        {
            cout << "Wrong Entry!" << endl;
            cin.clear();
            cin.ignore(100, '\n');
        }
        else
        {
            printEntry(staffTWB);
            //printArray(staffTWB, 50);
            // thought was to grab the final result into the array and then print but couldn't figure out
            cin.clear();
            cin.ignore(100, '\n');
        }
        //}

    } while (true);
    return 0;
}

// I was thinking of doing a for loop with each printEntry but couldn't figure out
