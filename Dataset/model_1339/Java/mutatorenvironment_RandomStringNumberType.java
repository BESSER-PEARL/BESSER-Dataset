





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_RandomStringNumberType extends StringType {

    private None max;
    private None min;
    private None allowsNull;



    public mutatorenvironment_RandomStringNumberType(
        None max,        None min,        None allowsNull    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.allowsNull = allowsNull;
    }


    public None getMax() {
        return max;
    }

    public void setMax(None max) {
        this.max = max;
    }
    public None getMin() {
        return min;
    }

    public void setMin(None min) {
        this.min = min;
    }
    public None getAllowsnull() {
        return allowsNull;
    }

    public void setAllowsnull(None allowsNull) {
        this.allowsNull = allowsNull;
    }


}