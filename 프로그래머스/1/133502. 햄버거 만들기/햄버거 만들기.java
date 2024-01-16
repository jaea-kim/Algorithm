import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] ingredient) {
        String pattern = "1231";
    
        int answer = 0;

        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < ingredient.length; i++) {
            stringBuilder.append(ingredient[i]);
            int length = stringBuilder.length();
            if (length > 3) {
                if (stringBuilder.subSequence(length - 4, length).equals(pattern)) {
                    stringBuilder.delete(length - 4, length);
                    answer += 1;
                }
            }
        }

        return answer;
    }
}