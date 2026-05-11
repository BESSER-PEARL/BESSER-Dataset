





import java.util.List;
import java.util.ArrayList;

public class iso20022_Binary extends DataType {

    private String length;
    private String minLength;
    private String maxLength;
    private String pattern;



    public iso20022_Binary(
        String length,        String minLength,        String maxLength,        String pattern    ) {
        super(
        );
        this.length = length;
        this.minLength = minLength;
        this.maxLength = maxLength;
        this.pattern = pattern;
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
    public String getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(String maxLength) {
        this.maxLength = maxLength;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }


}