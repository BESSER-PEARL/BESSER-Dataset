





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Transition extends Element {

    private int minTime;
    private int maxTime;



    public PetriNet_Transition(
        int minTime,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.maxTime = maxTime;
    }


    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }


}