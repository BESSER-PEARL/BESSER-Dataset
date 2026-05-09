





import java.util.List;
import java.util.ArrayList;

public class occi_StringType extends BasicType {

    private String maxLength;
    private String length;
    private String pattern;
    private String minLength;



    public occi_StringType(
        String maxLength,        String length,        String pattern,        String minLength    ) {
        super(
        );
        this.maxLength = maxLength;
        this.length = length;
        this.pattern = pattern;
        this.minLength = minLength;
    }


    public String getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(String maxLength) {
        this.maxLength = maxLength;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getMinlength() {
        return minLength;
    }

    public void setMinlength(String minLength) {
        this.minLength = minLength;
    }


}