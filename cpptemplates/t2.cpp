#include<iostream>

template<class T>
const T& pe_max(const T& a, const T& b)
{
    return a>=b ? a : b;
};
char pe_max(char a, int b) { return pe_max<char>(a, b); }

int main(int argc, char*argv[])
{
    using namespace std;

    cout << pe_max(1,2) << endl;
    cout << pe_max<char>('a', 2) << endl;
    cout << pe_max('b', 'a') << endl;
}