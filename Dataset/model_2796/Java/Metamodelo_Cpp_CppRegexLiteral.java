





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppRegexLiteral extends CppExpression {

    private String options;
    private String pattern;



    public Metamodelo_Cpp_CppRegexLiteral(
        String options,        String pattern    ) {
        super(
        );
        this.options = options;
        this.pattern = pattern;
    }


    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }


}