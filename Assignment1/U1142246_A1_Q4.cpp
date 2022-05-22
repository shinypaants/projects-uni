#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{

    string movies[5];
    string genre[5];
    int rate[5];

    ifstream inFile;
    inFile.open("q4data.txt", ios::in);
    while (inFile)
    {
        for (int i = 0; i < 5; i++)
        {
            // getline should work and it is saying no matching function for call to 'getline'
            getline(cin, movies[i]);
            getline(cin, genre[i]);
            getline(cin, rate[i]);
        }
        // string qual[5];
        // if code worked the way i'd check for the quality is like Q3.
        // if (rate >= 3.5)
        // {
        //append into qual
        //    cout << "Good"
        // }
        // else if (rate > 2.0 && < 3.5)
        //  {
        //append into qual
        //    cout << "OK"
        //  }
        //  else
        //  {
        //apend into qual
        //     cout << "Not Good"
    }

    cout << "1234567890123456789012345678901234567890123456789012345678901234567890" << endl;

    for (int i = 0; i < 5; i++)
    {
        cout << setw(30) << movies[i] << setw(20) << genre[i] << setprecision(1) << fixed << setw(5) << rate[i] << endl;
    }
    cout << "1234567890123456789012345678901234567890123456789012345678901234567890" << endl;
}