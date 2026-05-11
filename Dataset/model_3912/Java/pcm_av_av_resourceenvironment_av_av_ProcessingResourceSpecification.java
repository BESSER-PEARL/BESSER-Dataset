





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification extends Identifier {

    private boolean requiredByContainer;
    private int numberOfReplicas;
    private float MTTF;
    private float MTTR;



    public pcm_av_av_resourceenvironment_av_av_ProcessingResourceSpecification(
        boolean requiredByContainer,        int numberOfReplicas,        float MTTF,        float MTTR    ) {
        super(
        );
        this.requiredByContainer = requiredByContainer;
        this.numberOfReplicas = numberOfReplicas;
        this.MTTF = MTTF;
        this.MTTR = MTTR;
    }


    public boolean getRequiredbycontainer() {
        return requiredByContainer;
    }

    public void setRequiredbycontainer(boolean requiredByContainer) {
        this.requiredByContainer = requiredByContainer;
    }
    public int getNumberofreplicas() {
        return numberOfReplicas;
    }

    public void setNumberofreplicas(int numberOfReplicas) {
        this.numberOfReplicas = numberOfReplicas;
    }
    public float getMttf() {
        return MTTF;
    }

    public void setMttf(float MTTF) {
        this.MTTF = MTTF;
    }
    public float getMttr() {
        return MTTR;
    }

    public void setMttr(float MTTR) {
        this.MTTR = MTTR;
    }


}