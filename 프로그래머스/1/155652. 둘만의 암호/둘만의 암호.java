import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {        
        List<Character> alphabet = new ArrayList<>();
        for (char i = 'a'; i <= 'z'; i++) {
            if (skip.indexOf(i) == -1) {
                alphabet.add(i);
            }
        }
        
        int alphabetL = alphabet.size();
        
        StringBuilder stringBuilder = new StringBuilder();
        for (char c : s.toCharArray()) {
            int i = alphabet.indexOf(c) + index;
            if (i >= alphabetL) {
                i = i % alphabetL;
            }
            stringBuilder.append(alphabet.get(i));
        }
        
        return stringBuilder.toString();
    }
}