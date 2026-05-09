





import java.util.List;
import java.util.ArrayList;

public class assessment_Url  {

    private String pattern;
    private String patternType;



    public assessment_Url(
        String pattern,        String patternType    ) {
        this.pattern = pattern;
        this.patternType = patternType;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getPatterntype() {
        return patternType;
    }

    public void setPatterntype(String patternType) {
        this.patternType = patternType;
    }


}