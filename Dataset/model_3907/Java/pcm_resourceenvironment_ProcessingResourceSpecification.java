





import java.util.List;
import java.util.ArrayList;

public class pcm_resourceenvironment_ProcessingResourceSpecification  {

    private float MTTR;
    private float MTTF;
    private String schedulingPolicy;





    private ProcessingResourceType processingresourcetype;


    public pcm_resourceenvironment_ProcessingResourceSpecification(
        float MTTR,        float MTTF,        String schedulingPolicy    ) {
        this.MTTR = MTTR;
        this.MTTF = MTTF;
        this.schedulingPolicy = schedulingPolicy;
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
    public String getSchedulingpolicy() {
        return schedulingPolicy;
    }

    public void setSchedulingpolicy(String schedulingPolicy) {
        this.schedulingPolicy = schedulingPolicy;
    }

    public ProcessingResourceType getProcessingresourcetype() {
        return processingresourcetype;
    }

    public void setProcessingresourcetype(ProcessingResourceType processingresourcetype) {
        this.processingresourcetype = processingresourcetype;
    }

}