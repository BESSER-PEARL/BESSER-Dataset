





import java.util.List;
import java.util.ArrayList;

public class iso20022_Binary extends DataType {

    private String pattern;
    private String maxLength;
    private String length;
    private String minLength;



    public iso20022_Binary(
        String pattern,        String maxLength,        String length,        String minLength    ) {
        super(
        );
        this.pattern = pattern;
        this.maxLength = maxLength;
        this.length = length;
        this.minLength = minLength;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
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
    public String getMinlength() {
        return minLength;
    }

    public void setMinlength(String minLength) {
        this.minLength = minLength;
    }


}