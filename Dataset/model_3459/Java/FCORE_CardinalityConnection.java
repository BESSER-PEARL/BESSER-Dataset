





import java.util.List;
import java.util.ArrayList;

public class FCORE_CardinalityConnection extends SingleFeatureConnection {

    private int max;
    private int min;



    public FCORE_CardinalityConnection(
        int max,        int min    ) {
        super(
        );
        this.max = max;
        this.min = min;
    }


    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }


}