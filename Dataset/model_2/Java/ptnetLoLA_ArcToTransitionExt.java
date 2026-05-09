





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_ArcToTransitionExt extends ArcToTransition {

    private float probability;



    public ptnetLoLA_ArcToTransitionExt(
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