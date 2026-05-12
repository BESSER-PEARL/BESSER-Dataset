





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_TransitionExt extends Transition {

    private int minTime;
    private String confidentiality;
    private int maxTime;
    private float probability;
    private float cost;



    public ptnetLoLA_TransitionExt(
        int minTime,        String confidentiality,        int maxTime,        float probability,        float cost    ) {
        super(
        );
        this.minTime = minTime;
        this.confidentiality = confidentiality;
        this.maxTime = maxTime;
        this.probability = probability;
        this.cost = cost;
    }


    public int getMintime() {
        return minTime;
    }

    public void setMintime(int minTime) {
        this.minTime = minTime;
    }
    public String getConfidentiality() {
        return confidentiality;
    }

    public void setConfidentiality(String confidentiality) {
        this.confidentiality = confidentiality;
    }
    public int getMaxtime() {
        return maxTime;
    }

    public void setMaxtime(int maxTime) {
        this.maxTime = maxTime;
    }
    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }
    public float getCost() {
        return cost;
    }

    public void setCost(float cost) {
        this.cost = cost;
    }


}