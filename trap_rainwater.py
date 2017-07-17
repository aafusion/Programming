
#include<iostream>

using namespace std;

int trapRainWaterCounter(int* array, int size)
{
    int left[size], right[size], water=0;

    left[0] = array[0];
    for(int i=1;i<size;i++) {
        left[i] = max(left[i-1], array[i]);
    }

    right[size-1] = array[size-1];
    for(int i=size-2;i>=0;i--) {
        right[i] = max(right[i+1], array[i]);
    }

    for(int i=0;i<size;i++) {
        water += min(left[i], right[i]) - array[i];
    }
    return water;
}

int main()
{
    //int array[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    int array[] = {3, 0, 0, 2, 0, 4};
    int water;
    cout << "Length : " << sizeof(array)/sizeof(*array);
    water = trapRainWaterCounter(array, sizeof(array)/sizeof(*array));

    cout << "Trapped water is : " << water << endl;
    return 0;
}
