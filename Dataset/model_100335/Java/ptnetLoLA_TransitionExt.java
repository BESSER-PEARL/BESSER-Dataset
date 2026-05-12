





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_TransitionExt extends Transition {

    private int minTime;
    private float probability;
    private int maxTime;
    private float cost;



    public ptnetLoLA_TransitionExt(
        int minTime,        float probability,        int maxTime,        float cost    ) {
        super(
        );
        this.minTime = minTime;
        this.probability = probability;
        this.maxTime = maxTime;
        this.cost = cost;
    }


    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }
    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }
    public float getCost() {
        return cost;
    }

    public void setCost(float cost) {
        this.cost = cost;
    }


}