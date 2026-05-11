





import java.util.List;
import java.util.ArrayList;

public class simpleALEnv_RandRange extends Arith {

    private int min;
    private int max;



    public simpleALEnv_RandRange(
        int min,        int max    ) {
        super(
        );
        this.min = min;
        this.max = max;
    }


    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }


}