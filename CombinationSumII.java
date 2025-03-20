import java.util.ArrayList;
import java.util.List;

public class CombinationSumII {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        result = backTrack(candidates, target, result, null)
        return result;

        
    }


    private List<List<Integer>> backTrack(int[] candidates, int target,List<List<Integer>> result, List<Integer> temp ) {

        return result;

    }
           
}
