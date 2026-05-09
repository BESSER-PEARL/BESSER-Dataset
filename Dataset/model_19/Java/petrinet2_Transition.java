





import java.util.List;
import java.util.ArrayList;

public class petrinet2_Transition extends Node {

    private float maxDelay;
    private float minDelay;



    public petrinet2_Transition(
        float maxDelay,        float minDelay    ) {
        super(
        );
        this.maxDelay = maxDelay;
        this.minDelay = minDelay;
    }


    public float getMaxdelay() {
        return maxDelay;
    }

    public void setMaxdelay(float maxDelay) {
        this.maxDelay = maxDelay;
    }
    public float getMindelay() {
        return minDelay;
    }

    public void setMindelay(float minDelay) {
        this.minDelay = minDelay;
    }


}