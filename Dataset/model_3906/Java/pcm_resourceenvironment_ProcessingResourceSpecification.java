





import java.util.List;
import java.util.ArrayList;

public class pcm_resourceenvironment_ProcessingResourceSpecification  {

    private String schedulingPolicy;





    private PCMRandomVariable pcmrandomvariable;




    private ProcessingResourceType processingresourcetype;


    public pcm_resourceenvironment_ProcessingResourceSpecification(
        String schedulingPolicy    ) {
        this.schedulingPolicy = schedulingPolicy;
    }


    public String getSchedulingpolicy() {
        return schedulingPolicy;
    }

    public void setSchedulingpolicy(String schedulingPolicy) {
        this.schedulingPolicy = schedulingPolicy;
    }

    public PCMRandomVariable getPcmrandomvariable() {
        return pcmrandomvariable;
    }

    public void setPcmrandomvariable(PCMRandomVariable pcmrandomvariable) {
        this.pcmrandomvariable = pcmrandomvariable;
    }
    public ProcessingResourceType getProcessingresourcetype() {
        return processingresourcetype;
    }

    public void setProcessingresourcetype(ProcessingResourceType processingresourcetype) {
        this.processingresourcetype = processingresourcetype;
    }

}