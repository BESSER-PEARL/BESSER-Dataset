





import java.util.List;
import java.util.ArrayList;

public class iso20022_Binary extends DataType {

    private String pattern;
    private String maxLength;
    private String minLength;
    private String length;



    public iso20022_Binary(
        String pattern,        String maxLength,        String minLength,        String length    ) {
        super(
        );
        this.pattern = pattern;
        this.maxLength = maxLength;
        this.minLength = minLength;
        this.length = length;
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
    public String getMinlength() {
        return minLength;
    }

    public void setMinlength(String minLength) {
        this.minLength = minLength;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }


}