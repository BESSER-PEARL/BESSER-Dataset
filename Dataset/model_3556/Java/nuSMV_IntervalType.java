





import java.util.List;
import java.util.ArrayList;

public class nuSMV_IntervalType extends SimpleType {

    private String low;
    private String high;



    public nuSMV_IntervalType(
        String low,        String high    ) {
        super(
        );
        this.low = low;
        this.high = high;
    }


    public String getLow() {
        return low;
    }

    public void setLow(String low) {
        this.low = low;
    }
    public String getHigh() {
        return high;
    }

    public void setHigh(String high) {
        this.high = high;
    }


}