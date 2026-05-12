





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition extends Node {

    private int min_time;
    private int max_time;



    public PetriNet_Transition(
        int min_time,        int max_time    ) {
        super(
        );
        this.min_time = min_time;
        this.max_time = max_time;
    }


    public int getMin_time() {
        return min_time;
    }

    public void setMin_time(int min_time) {
        this.min_time = min_time;
    }
    public int getMax_time() {
        return max_time;
    }

    public void setMax_time(int max_time) {
        this.max_time = max_time;
    }


}