





import java.util.List;
import java.util.ArrayList;

public class iso20022_Boolean extends DataType {

    private String pattern;



    public iso20022_Boolean(
        String pattern    ) {
        super(
        );
        this.pattern = pattern;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }


}