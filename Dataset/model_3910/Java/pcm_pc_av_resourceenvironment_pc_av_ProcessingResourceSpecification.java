





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification extends Identifier {

    private float MTTF;
    private int numberOfReplicas;
    private boolean requiredByContainer;
    private float MTTR;



    public pcm_pc_av_resourceenvironment_pc_av_ProcessingResourceSpecification(
        float MTTF,        int numberOfReplicas,        boolean requiredByContainer,        float MTTR    ) {
        super(
        );
        this.MTTF = MTTF;
        this.numberOfReplicas = numberOfReplicas;
        this.requiredByContainer = requiredByContainer;
        this.MTTR = MTTR;
    }


    public float getMttf() {
        return MTTF;
    }

    public void setMttf(float MTTF) {
        this.MTTF = MTTF;
    }
    public int getNumberofreplicas() {
        return numberOfReplicas;
    }

    public void setNumberofreplicas(int numberOfReplicas) {
        this.numberOfReplicas = numberOfReplicas;
    }
    public boolean getRequiredbycontainer() {
        return requiredByContainer;
    }

    public void setRequiredbycontainer(boolean requiredByContainer) {
        this.requiredByContainer = requiredByContainer;
    }
    public float getMttr() {
        return MTTR;
    }

    public void setMttr(float MTTR) {
        this.MTTR = MTTR;
    }


}