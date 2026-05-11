





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_InternalAction extends AbstractResourceDemandingAction {

    private String failureProbability;



    public pcm_seff_InternalAction(
        String failureProbability    ) {
        super(
        );
        this.failureProbability = failureProbability;
    }


    public String getFailureprobability() {
        return failureProbability;
    }

    public void setFailureprobability(String failureProbability) {
        this.failureProbability = failureProbability;
    }


}