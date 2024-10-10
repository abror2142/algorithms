#include <iostream>
#include <unordered_map>

using namespace std;

int fibNaive(int);

long long int fibOptimized(int, unordered_map<int, long long int>&);


int main()
{
    int n = 12; // Chosen Fibonacci number
    unordered_map<int, long long int>ump; // Used for memoization in Optimized Approach
    cout << "\t>>>>nth Fibonacci Number using<<<<" << endl; 

    cout << "Naive Algorithm: n=" << n << "\t= " << fibNaive(n) << endl;
    cout << "Optimized Algorithm: n=" << n << "\t= " << fibOptimized(n, ump) << endl;

    return 0;
}


int fibNaive(int n)
{
    if(n <= 2) return 1;
    return fibNaive(n-1) + fibNaive(n-2);
}

long long int fibOptimized(int n, unordered_map<int, long long int>&ump)
{
    if(ump.find(n) != ump.end()) return ump[n];

    if(n <= 2) return 1;

    ump[n] = fibOptimized(n-1, ump) + fibOptimized(n-2, ump);
    return ump[n];
}