#include <iostream>
#include <vector>

using namespace std;


// unordered set solution can be possible too!
bool canSum(int, vector<int>, unordered_map<int, int> &, int);

bool canSumOptimized(int, vector<int>, unordered_map<int, int> &);

int main(int argc, char * argv[])
{
    int target = 18;
    vector<int> array = {3, 7};
    unordered_map<int, int> memo;

    // sum will be attached to the memo as key, the arr element will be 
    // value which means that this value is reachable with this array element;
    int sum = 0;

    cout << canSumOptimized(target, array, memo) << endl;

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

// From tutorial My solution turned out to be not so effective!
// There is better approach even tough my approach can be similar
bool canSumOptimized(int target, vector<int>array, unordered_map<int, int> &memo)
{
    if(memo.find(target) != memo.end()) return memo[target]; // here is the trick!
    // Instead of storing calcualted value of the subtree we can use it store bool value of sub tree.
    if(target == 0) return true;
    if(target < 0) return false;

    for(int i=0; i<array.size(); i++)
    {
        int new_target = target - array[i];
        
        if(canSumOptimized(new_target, array, memo))
        {
            memo[target] = true;
            return true;
        }
    }

    memo[target] = false;
    return false;
}
