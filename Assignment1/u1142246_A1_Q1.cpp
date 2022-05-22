#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

const string movies[5] = {"The Batman", "Monster Family 2", "The Duke", "The Bad Guy", "The Godfather"};
const string genres[5] = {"Action", "Animation", "Comedy", "Animation", "Drama"};
const float rates[5] = {4.5, 3.1, 2.0, 1.2, 4.8};
const string qualities[5] = {"Good", "OK", "Not Good", "Not Good", "Good"};

int main()
{
    cout << "1234567890123456789012345678901234567890123456789012345678901234567890" << endl;

    for (int i = 0; i < 5; i++)
    {
        cout << setw(30) << movies[i] << setw(20) << genres[i] << setprecision(1) << fixed << setw(5) << rates[i] << setw(15) << qualities[i] << endl;
    }
    cout << "1234567890123456789012345678901234567890123456789012345678901234567890" << endl;
}