#include <iostream>
#include <unordered_map>

using namespace std;

int pathNaive(pair<int, int>);

// pair<int, int> needs hash function to be used inside unordered_map as a key!
struct PairHashFunction{
    std::size_t operator() (const std::pair<int, int> &v) const
    {
        return hash<int>()(v.first) ^ hash<int>()(v.second);
    }
};

long long int pathOptimized(pair<int, int>, unordered_map<pair<int, int>, long long int, PairHashFunction> &);


int main(int argc, char * argv[])
{
    pair<int, int> grid(4, 4); // Grid size defined as pair (doesn't have to be the same number)

    cout << "\t>>>>Number of path from top-left to bottom right inside Grid<<<<" << endl; 
    unordered_map<pair<int, int>, long long int, PairHashFunction> memo;

    cout << "Naive Algorithm:     grid=(" << grid.first << ", " << grid.second << ")\t=> " << pathNaive(grid) << endl;
    cout << "Optimized Algorithm: grid=(" << grid.first << ", " << grid.second << ")\t=> " << pathOptimized(grid, memo) << endl;

    return 0;
};


int pathNaive(pair<int, int>grid)
{
    // this algorithm can't find number of path as the grid size increses
    if(grid.first == 0 || grid.second == 0)
        return 0;
    
    if(grid.first == 1 && grid.second == 1)
        return 1;

    pair<int, int>grid1(grid.first-1, grid.second);  // one part
    pair<int, int>grid2(grid.first, grid.second-1);  // another part

    return pathNaive(grid1) + pathNaive(grid2);
}

long long int pathOptimized(pair<int, int>grid, unordered_map<pair<int, int>, long long int, PairHashFunction> &memo)
{
    // pair defines (x, y)
    if(memo.find(grid) != memo.end())
        return memo[grid];  // if the path already calculated use that value

    if(grid.first == 0 || grid.second == 0)
        return 0;  // can't have grid with 0
    
    if(grid.first == 1 && grid.second == 1)
        return 1;  // base case

    pair<int, int>grid1(grid.first-1, grid.second);  // going down (by x-1)
    pair<int, int>grid2(grid.first, grid.second-1);  // going right (by y-1)

    memo[grid] = pathOptimized(grid1, memo) + pathOptimized(grid2, memo); // save in memo
    return memo[grid];
}
