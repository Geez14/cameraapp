import java.util.regex.Pattern;
class Test {
  public static void main(String[] args) {
    // +? is good approach in future we get benifits!!
    Pattern p = Pattern.compile("(.+?)(\\.[\\w]*$|$)");
    int i = 0;
    java.util.regex.Matcher m = p.matcher("");
    while (m.find()) {
      System.out.print(m.group());
    }
    System.out.println();
    System.out.println(m.matches());
  }
}