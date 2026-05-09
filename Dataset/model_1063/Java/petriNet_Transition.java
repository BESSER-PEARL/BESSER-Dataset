





import java.util.List;
import java.util.ArrayList;

public class petriNet_Transition extends Node {

    private int max_time;
    private int min_time;



    public petriNet_Transition(
        int max_time,        int min_time    ) {
        super(
        );
        this.max_time = max_time;
        this.min_time = min_time;
    }


    public int getMax_time() {
        return max_time;
    }

    public void setMax_time(int max_time) {
        this.max_time = max_time;
    }
    public int getMin_time() {
        return min_time;
    }

    public void setMin_time(int min_time) {
        this.min_time = min_time;
    }


}