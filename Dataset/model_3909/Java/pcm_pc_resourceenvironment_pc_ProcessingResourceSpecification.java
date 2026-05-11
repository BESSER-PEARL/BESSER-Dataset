





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification extends Identifier {

    private boolean requiredByContainer;
    private float MTTF;
    private int numberOfReplicas;
    private float MTTR;



    public pcm_pc_resourceenvironment_pc_ProcessingResourceSpecification(
        boolean requiredByContainer,        float MTTF,        int numberOfReplicas,        float MTTR    ) {
        super(
        );
        this.requiredByContainer = requiredByContainer;
        this.MTTF = MTTF;
        this.numberOfReplicas = numberOfReplicas;
        this.MTTR = MTTR;
    }


    public boolean getRequiredbycontainer() {
        return requiredByContainer;
    }

    public void setRequiredbycontainer(boolean requiredByContainer) {
        this.requiredByContainer = requiredByContainer;
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
    public float getMttr() {
        return MTTR;
    }

    public void setMttr(float MTTR) {
        this.MTTR = MTTR;
    }


}