





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeRegexLiteral extends HaxeConstant {

    private String options;
    private String pattern;



    public haxe_HaxeRegexLiteral(
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