





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Indicator extends XSDBoolean {

    private String pattern;
    private String meaningWhenTrue;
    private String meaningWhenFalse;



    public ISO20022_Indicator(
        String pattern,        String meaningWhenTrue,        String meaningWhenFalse    ) {
        super(
        );
        this.pattern = pattern;
        this.meaningWhenTrue = meaningWhenTrue;
        this.meaningWhenFalse = meaningWhenFalse;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getMeaningwhentrue() {
        return meaningWhenTrue;
    }

    public void setMeaningwhentrue(String meaningWhenTrue) {
        this.meaningWhenTrue = meaningWhenTrue;
    }
    public String getMeaningwhenfalse() {
        return meaningWhenFalse;
    }

    public void setMeaningwhenfalse(String meaningWhenFalse) {
        this.meaningWhenFalse = meaningWhenFalse;
    }


}