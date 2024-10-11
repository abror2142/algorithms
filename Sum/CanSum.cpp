#include <iostream>
#include <vector>

using namespace std;


// unordered set solution can be possible too!
bool canSum(int, vector<int>, unordered_map<int, int> &, int);

int main(int argc, char * argv[])
{
    int target = 10;
    vector<int> array = {3, 7};
    unordered_map<int, int> memo;

    // sum will be attached to the memo as key, the arr element will be 
    // value which means that this value is reachable with this array element;
    int sum = 0; cout << canSum(target, array, memo, sum) << endl;

    return 0;
}

// my own implementation :) May not be optimal!
bool canSum(int target, vector<int>array, unordered_map<int, int> &memo, int sum)
{
    if(memo.find(target) != memo.end()) return true;

    for(int i=0; i<array.size(); i++)
    {
        if(target - array[i] > 0)
        {
            int temp_sum = sum + array[i];
            memo[temp_sum] = array[i];
            bool val = canSum(target-array[i], array, memo, temp_sum);
            if(val)
                return true;
        }
        if(target - array[i] == 0)
            return true;
    }
    return false;
}