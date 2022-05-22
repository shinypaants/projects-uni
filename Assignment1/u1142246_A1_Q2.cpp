#include <iostream>
#include <string>
#include <iomanip>
#include <vector>

using namespace std;

// I tried so many times to figure this out with different functions like void
// Could not get things to work and the program kept shutting off after the first and wouldn't let me continue to answer the question
//

int main()
{
    vector<int> movieNum;

    cout << "Please enter number of integers: " << endl;
    cin >> movieNum;

    vector<string> movieName[movieNum];
    vector<string> movieGenre[movieNum];
    vector<string> movieRate[movieNum];
    vector<string> movieQual[movieNum];
    // this is as close as i could get to be able to hold the final product
    for (int i = 0; i < movieNum; i++)
    {
        cout << "Please enter movie name: " << endl;
        cin >> movieName[i] << movieName.pushback();
        for (int x = 0; x < movieNum; x++)
        {
            cout << "Please enter genre and rating: " << endl;
            cin >> movieGenre[x] >> movieRate[x] >> movieQual[x];
        }
    }

    // i will show what it will look like anyway at the end with predefined array etc.
    const string movies[5] = {"The Batman", "Monster Family 2", "The Duke", "The Bad Guy", "The Godfather"};
    const string genres[5] = {"Action", "Animation", "Comedy", "Animation", "Drama"};
    const float rates[5] = {4.5, 3.1, 2.0, 1.2, 4.8};
    const string qualities[5] = {"Good", "OK", "Not Good", "Not Good", "Good"};

    cout << "1234567890123456789012345678901234567890123456789012345678901234567890" << endl;

    for (int y = 0; y < 5; y++)
    {
        cout << left << setw(30) << movies[y] << left << setw(20) << genres[y] << setprecision(1) << fixed << left << setw(5) << rates[y] << left << setw(15) << qualities[y] << endl;
    }
    cout << "1234567890123456789012345678901234567890123456789012345678901234567890" << endl;
}