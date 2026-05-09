





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_TransitionExt extends Transition {

    private String confidentiality;
    private int maxTime;
    private float probability;
    private int minTime;
    private float cost;



    public ptnetLoLA_TransitionExt(
        String confidentiality,        int maxTime,        float probability,        int minTime,        float cost    ) {
        super(
        );
        this.confidentiality = confidentiality;
        this.maxTime = maxTime;
        this.probability = probability;
        this.minTime = minTime;
        this.cost = cost;
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


}