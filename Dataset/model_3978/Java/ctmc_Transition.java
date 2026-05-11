





import java.util.List;
import java.util.ArrayList;

public class ctmc_Transition extends IDBase {

    private float rate;
    private float prob;



    public ctmc_Transition(
        float rate,        float prob    ) {
        super(
        );
        this.rate = rate;
        this.prob = prob;
    }


    public float getRate() {
        return rate;
    }

    public void setRate(float rate) {
        this.rate = rate;
    }
    public float getProb() {
        return prob;
    }

    public void setProb(float prob) {
        this.prob = prob;
    }


}