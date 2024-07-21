class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Let num1 + num2 = target
        // Let i be index of num1
        //Let j be index of num2
        int[] ans = {0,0};
        for(int i = 0; i< nums.length;i++){
            int num1 = nums[i];
            for(int j = i+1; j < nums.length;j++){
                int num2 = nums[j];
                if(num1+num2 == target){
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }
        return ans;
    }
}