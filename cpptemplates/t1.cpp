#include<iostream>

template<class T>
class Num
{
public:
    T _x;
    Num(T x): _x(x) {};
    operator T() { return _x; };
};

template<class T>
T f(T a) { return(a+1); };

template<class T>
Num<T> f(Num<T> a) { return(a+2); };

int f(int a) { return(a+4); };

int main(int argc, char*argv[])
{
    std::cout << f(Num<int>(1)) << std::endl;
    std::cout << f(1) << std::endl;
}