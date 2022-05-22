#include <iostream>
#include <string>
#include <iomanip>
#include <vector>

using namespace std;

// Pretty hard to do when I couldn't complete Q2 as that would help a lot but this is the best
// I could do to give you an idea of what I would have done if I could finish Q2.
// I hope this show the effort im trying to put in.

int main()
{
    string movieName[5] = {" "};
    string movieGenre[5] = {"Action", "Animation", "Comedy", "Animation", "Drama"};
    int movieRate;
    string movieQual;

    int counter = 0;
    while (counter < 5)
    {
        cout << "Please enter movie name: " >> ;
        counter++;
        movieName[counter];
        cout << "Please enter genre and rating: ";
        if (movieRate >= 3.5)
        {
            //append into movieQual
            cout << "Good"
        }
        else if (movieRate > 2.0 && < 3.5)
        {
            //append into movieQual
            cout << "OK"
        }
        else
        {
            //apend into movieQual
            cout << "Not Good"
        }
    }
}