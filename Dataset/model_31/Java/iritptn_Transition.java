





import java.util.List;
import java.util.ArrayList;

public class iritptn_Transition extends Node {

    private int tMax;
    private int tMin;



    public iritptn_Transition(
        int tMax,        int tMin    ) {
        super(
        );
        this.tMax = tMax;
        this.tMin = tMin;
    }


    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }
    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }


}