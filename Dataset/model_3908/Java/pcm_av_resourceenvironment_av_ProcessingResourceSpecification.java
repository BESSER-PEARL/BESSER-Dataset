





import java.util.List;
import java.util.ArrayList;

public class pcm_av_resourceenvironment_av_ProcessingResourceSpecification extends Identifier {

    private float MTTF;
    private int numberOfReplicas;
    private float MTTR;
    private boolean requiredByContainer;



    public pcm_av_resourceenvironment_av_ProcessingResourceSpecification(
        float MTTF,        int numberOfReplicas,        float MTTR,        boolean requiredByContainer    ) {
        super(
        );
        this.MTTF = MTTF;
        this.numberOfReplicas = numberOfReplicas;
        this.MTTR = MTTR;
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
    public boolean getRequiredbycontainer() {
        return requiredByContainer;
    }

    public void setRequiredbycontainer(boolean requiredByContainer) {
        this.requiredByContainer = requiredByContainer;
    }


}