





import java.util.List;
import java.util.ArrayList;

public class xtextTest_ReplacePatterns  {

    private String replace;
    private String regex;





    private xtextTest_Generator xtexttest_generator;


    public xtextTest_ReplacePatterns(
        String replace,        String regex    ) {
        this.replace = replace;
        this.regex = regex;
    }


    public String getReplace() {
        return replace;
    }

    public void setReplace(String replace) {
        this.replace = replace;
    }
    public String getRegex() {
        return regex;
    }

    public void setRegex(String regex) {
        this.regex = regex;
    }

    public xtextTest_Generator getXtexttest_generator() {
        return xtexttest_generator;
    }

    public void setXtexttest_generator(xtextTest_Generator xtexttest_generator) {
        this.xtexttest_generator = xtexttest_generator;
    }

}