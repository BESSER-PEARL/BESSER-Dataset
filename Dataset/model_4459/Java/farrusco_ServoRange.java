





import java.util.List;
import java.util.ArrayList;

public class farrusco_ServoRange extends Actuate {

    private int max;
    private int min;
    private int inc;



    public farrusco_ServoRange(
        int max,        int min,        int inc    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.inc = inc;
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
    public int getInc() {
        return inc;
    }

    public void setInc(int inc) {
        this.inc = inc;
    }


}