





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_RandomStringType extends StringType {

    private None min;
    private None max;
    private None allowsNull;



    public mutatorenvironment_RandomStringType(
        None min,        None max,        None allowsNull    ) {
        super(
        );
        this.min = min;
        this.max = max;
        this.allowsNull = allowsNull;
    }


    public None getMin() {
        return min;
    }

    public void setMin(None min) {
        this.min = min;
    }
    public None getMax() {
        return max;
    }

    public void setMax(None max) {
        this.max = max;
    }
    public None getAllowsnull() {
        return allowsNull;
    }

    public void setAllowsnull(None allowsNull) {
        this.allowsNull = allowsNull;
    }


}