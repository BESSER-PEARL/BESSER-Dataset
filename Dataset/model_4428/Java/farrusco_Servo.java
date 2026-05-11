





import java.util.List;
import java.util.ArrayList;

public class farrusco_Servo extends Actuate {

    private int inc;
    private int max;
    private int min;



    public farrusco_Servo(
        int inc,        int max,        int min    ) {
        super(
        );
        this.inc = inc;
        this.max = max;
        this.min = min;
    }


    public int getInc() {
        return inc;
    }

    public void setInc(int inc) {
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


}