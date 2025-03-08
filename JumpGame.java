public class JumpGame {

    public boolean canJump(int[] nums) {


        if (nums.length == 1 && nums[0] >= 0) {
            return true;
        }
        

        int index = nums.length - 1;
        int max  = 0;
        for (int i = 0; i < index ; i++) {

            if (i > max) {
            return false;  
            }
            
            max = Math.max(max, i + nums[i]);

            if (max >= index) {
                return true;
            }
            
    
        }
        return false;
    }



    public static void main(String[] args) {
        JumpGame jumpGame = new JumpGame();

        // Test cases
        int[][] testCases = {
            {3,2,1,0,4},  // Expected: false
            
        };

        
            
            System.out.println(jumpGame.canJump(testCases[0]));
        
    }
}    


