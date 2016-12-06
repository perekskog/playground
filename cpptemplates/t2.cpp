#include<iostream>

template<class T>
const T& pe_max(const T& a, const T& b)
{
    if(a>=b)
        return a;
    else
        return b;
};
char pe_max(char a, int b)
{
    return pe_max(a, static_cast<char>(b));
}


int main(int argc, char*argv[])
{
    using namespace std;

    cout << pe_max(1,2) << endl;
    cout << pe_max('a', 2) << endl;
    cout << pe_max('b', 'a') << endl;
}