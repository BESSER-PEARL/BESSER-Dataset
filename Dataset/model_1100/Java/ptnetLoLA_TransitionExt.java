





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_TransitionExt extends Transition {

    private int minTime;
    private float cost;
    private float probability;
    private int maxTime;



    public ptnetLoLA_TransitionExt(
        int minTime,        float cost,        float probability,        int maxTime    ) {
        super(
        );
        this.minTime = minTime;
        this.cost = cost;
        this.probability = probability;
        this.maxTime = maxTime;
    }


    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public float getCost() {
        return cost;
    }

    public void setCost(float cost) {
        this.cost = cost;
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


}