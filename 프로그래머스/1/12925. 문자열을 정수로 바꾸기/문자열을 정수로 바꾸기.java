class Solution {
    public int solution(String s) {
        if (s.startsWith("+")) {
            return Integer.parseInt(s.substring(1, s.length()));
        } 
        return Integer.parseInt(s);
        
    }
}