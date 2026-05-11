





import java.util.List;
import java.util.ArrayList;

public class jkind_SubrangeType extends Type {

    private String high;
    private String low;



    public jkind_SubrangeType(
        String high,        String low    ) {
        super(
        );
        this.high = high;
        this.low = low;
    }


    public String getHigh() {
        return high;
    }

    public void setHigh(String high) {
        this.high = high;
    }
    public String getLow() {
        return low;
    }

    public void setLow(String low) {
        this.low = low;
    }


}