





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_InternalAction extends AbstractInternalControlFlowAction {

    private float failureProbability;



    public pcm_seff_InternalAction(
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