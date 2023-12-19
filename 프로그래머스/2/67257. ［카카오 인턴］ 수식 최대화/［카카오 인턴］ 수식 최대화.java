import java.util.*;

class Solution {
  public long solution(String expression) {
        List<String> elements = new ArrayList<>();
        StringBuilder number = new StringBuilder();

        String[] chars = expression.split("");

        Set<String> o = new HashSet<>();
        for (String c : chars) {
            if (c.equals("*")) {
                elements.add(number.toString());
                number.delete(0, number.length());
                o.add("*");
                elements.add("*");
            } else if (c.equals("+")) {
                elements.add(number.toString());
                number.delete(0, number.length());
                o.add("+");
                elements.add("+");
            } else if (c.equals("-")) {
                elements.add(number.toString());
                number.delete(0, number.length());
                o.add("-");
                elements.add("-");
            } else {
                number.append(c);
            }
        }
        elements.add(number.toString());
        List<String> operator = new ArrayList<>(o);

        if (operator.size() == 1) {
            long answer = Long.parseLong(elements.get(0));
            if (operator.get(0).equals("*")) {
                for (int i = 2; i < elements.size(); i+=2) {
                    answer = answer * Long.parseLong(elements.get(i));
                }
            } else if (operator.get(0).equals("+")) {
                for (int i = 2; i < elements.size(); i+=2) {
                    answer = answer + Long.parseLong(elements.get(i));
                }
            } else if (operator.get(0).equals("-")) {
                for (int i = 2; i < elements.size(); i+=2) {
                    answer = answer - Long.parseLong(elements.get(i));
                }
            }
            return Math.abs(answer);
        }

        List<Long> results = new ArrayList<>();
        if (operator.size() == 2) {
            //우선순위 반복
            for (int i = 0; i < 2; i++) {
                //연산 반복
                List<String> copyElements = new ArrayList<>(elements);
                for (int j = 0; j < 2; j++) {
                    while (true) {
                        if (copyElements.size() == 1) {
                            results.add(Math.abs(Long.parseLong(copyElements.get(0))));
                            break;
                        }
                        int index = copyElements.indexOf(operator.get(j));
                        if (index == -1) {
                            break;
                        }
                        long result = calculate(copyElements.get(index), copyElements.get(index - 1), copyElements.get(index + 1));
                        copyElements.remove(index + 1);
                        copyElements.remove(index);
                        copyElements.remove(index - 1);
                        copyElements.add(index - 1, String.valueOf(result));
                    }
                }
                Collections.reverse(operator);
            }
        }

        if (operator.size() == 3) {
            //우선순위 반복
            List<List<String>> cases = new ArrayList<>(List.of(List.of("+", "-", "*"), List.of("+", "*", "-"), List.of("-", "+", "*"), List.of("-", "*", "+"), List.of("*", "+", "-"), List.of("*", "-", "+")));
            for (int i = 0; i < cases.size(); i++) {
                //연산 반복
                List<String> copyElements = new ArrayList<>(elements);
                for (int j = 0; j < 3; j++) {
                    while (true) {
                        if (copyElements.size() == 1) {
                            results.add(Math.abs(Long.parseLong(copyElements.get(0))));
                            break;
                        }
                        int index = copyElements.indexOf(cases.get(i).get(j));
                        if (index == -1) {
                            break;
                        }
                        long result = calculate(copyElements.get(index), copyElements.get(index - 1), copyElements.get(index + 1));
                        copyElements.remove(index + 1);
                        copyElements.remove(index);
                        copyElements.remove(index - 1);
                        copyElements.add(index - 1, String.valueOf(result));
                    }
                }
            }
        }

        results.sort(Comparator.reverseOrder());
        return results.get(0);
    }

    public long calculate(String operator, String a, String b) {
        if (operator.equals("*")) {
            return multiply(a, b);
        } else if (operator.equals("+")) {
            return plus(a, b);
        } else {
            return minus(a, b);
        }
    }

    public long plus(String a, String b) {
        return Long.parseLong(a) + Long.parseLong(b);
    }

    public long minus(String a, String b) {
        return Long.parseLong(a) - Long.parseLong(b);
    }

    public long multiply(String a, String b) {
        return Long.parseLong(a) * Long.parseLong(b);
    }
}