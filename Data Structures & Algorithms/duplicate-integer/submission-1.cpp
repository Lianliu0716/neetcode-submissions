#include <map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int>count = {};
        for(int i = 0;i<nums.size();i++){
            if(i==0){
                count.insert({nums[i],1});
                continue;
            }
            auto find = count.find(nums[i]);
            if(find == count.end()){
                count.insert({nums[i],1});
            }
            else{
                return true;
            }
        }
        return false;

    }
};