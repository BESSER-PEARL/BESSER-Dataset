





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification extends Identifier {

    private boolean requiredByContainer;
    private float MTTR;
    private float MTTF;
    private int numberOfReplicas;



    public pcm_pc_pc_resourceenvironment_pc_pc_ProcessingResourceSpecification(
        boolean requiredByContainer,        float MTTR,        float MTTF,        int numberOfReplicas    ) {
        super(
        );
        this.requiredByContainer = requiredByContainer;
        this.MTTR = MTTR;
        this.MTTF = MTTF;
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


}