





import java.util.List;
import java.util.ArrayList;

public class iso20022_String extends DataType {

    private String pattern;
    private String length;
    private String maxLength;
    private String minLength;



    public iso20022_String(
        String pattern,        String length,        String maxLength,        String minLength    ) {
        super(
        );
        this.pattern = pattern;
        this.length = length;
        this.maxLength = maxLength;
        this.minLength = minLength;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(String maxLength) {
        this.maxLength = maxLength;
    }
    public String getMinlength() {
        return minLength;
    }

    public void setMinlength(String minLength) {
        this.minLength = minLength;
    }


}