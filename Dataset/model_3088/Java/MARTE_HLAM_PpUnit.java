





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_PpUnit  {

    private String concPolicy;
    private String memorySize;





    private HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier;


    public MARTE_HLAM_PpUnit(
        String concPolicy,        String memorySize    ) {
        this.concPolicy = concPolicy;
        this.memorySize = memorySize;
    }


    public String getConcpolicy() {
        return concPolicy;
    }

    public void setConcpolicy(String concPolicy) {
        this.concPolicy = concPolicy;
    }
    public String getMemorysize() {
        return memorySize;
    }

    public void setMemorysize(String memorySize) {
        this.memorySize = memorySize;
    }

    public HLAM_MARTE_BehavioredClassifier getHlam_marte_behavioredclassifier() {
        return hlam_marte_behavioredclassifier;
    }

    public void setHlam_marte_behavioredclassifier(HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier) {
        this.hlam_marte_behavioredclassifier = hlam_marte_behavioredclassifier;
    }

}