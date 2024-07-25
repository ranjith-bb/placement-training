public class Palindrome {
    public static void main(String[] args) {
        String str = "madam";
        boolean isPalindrome = str.equals(new StringBuilder(str).reverse().toString());
        System.out.println("Is palindrome: " + isPalindrome);
    }
}
