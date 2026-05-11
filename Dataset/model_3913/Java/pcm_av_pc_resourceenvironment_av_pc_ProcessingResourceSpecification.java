





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification extends Identifier {

    private boolean requiredByContainer;
    private float MTTF;
    private float MTTR;
    private int numberOfReplicas;





    private SchedulingPolicy schedulingpolicy;




    private ProcessingResourceType processingresourcetype;


    public pcm_av_pc_resourceenvironment_av_pc_ProcessingResourceSpecification(
        boolean requiredByContainer,        float MTTF,        float MTTR,        int numberOfReplicas    ) {
        super(
        );
        this.requiredByContainer = requiredByContainer;
        this.MTTF = MTTF;
        this.MTTR = MTTR;
        this.numberOfReplicas = numberOfReplicas;
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
    public float getMttr() {
        return MTTR;
    }

    public void setMttr(float MTTR) {
        this.MTTR = MTTR;
    }
    public int getNumberofreplicas() {
        return numberOfReplicas;
    }

    public void setNumberofreplicas(int numberOfReplicas) {
        this.numberOfReplicas = numberOfReplicas;
    }

    public SchedulingPolicy getSchedulingpolicy() {
        return schedulingpolicy;
    }

    public void setSchedulingpolicy(SchedulingPolicy schedulingpolicy) {
        this.schedulingpolicy = schedulingpolicy;
    }
    public ProcessingResourceType getProcessingresourcetype() {
        return processingresourcetype;
    }

    public void setProcessingresourcetype(ProcessingResourceType processingresourcetype) {
        this.processingresourcetype = processingresourcetype;
    }

}