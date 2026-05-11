





import java.util.List;
import java.util.ArrayList;

public class ISO20022_XSDBinary extends DataType {

    private String maxLength;
    private String minLength;
    private String length;
    private String pattern;



    public ISO20022_XSDBinary(
        String maxLength,        String minLength,        String length,        String pattern    ) {
        super(
        );
        this.maxLength = maxLength;
        this.minLength = minLength;
        this.length = length;
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
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }


}