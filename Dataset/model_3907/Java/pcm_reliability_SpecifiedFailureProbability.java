





import java.util.List;
import java.util.ArrayList;

public class pcm_reliability_SpecifiedFailureProbability extends SpecifiedQoSAnnotation {

    private float failureProbability;



    public pcm_reliability_SpecifiedFailureProbability(
        float failureProbability    ) {
        super(
        );
        this.failureProbability = failureProbability;
    }


    public float getFailureprobability() {
        return failureProbability;
    }

    public void setFailureprobability(float failureProbability) {
        this.failureProbability = failureProbability;
    }


}