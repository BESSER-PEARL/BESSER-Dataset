





import java.util.List;
import java.util.ArrayList;

public class faultTree_ProbabalisticEvent extends Event {

    private float probability;



    public faultTree_ProbabalisticEvent(
        float probability    ) {
        super(
        );
        this.probability = probability;
    }


    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }


}