





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_RtSpecification  {

    private String absDl;
    private String rdTime;
    private String utility;
    private String relDl;
    private String priority;
    private String miss;
    private String occKind;
    private String boundDl;





    private HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature;


    public MARTE_HLAM_RtSpecification(
        String absDl,        String rdTime,        String utility,        String relDl,        String priority,        String miss,        String occKind,        String boundDl    ) {
        this.absDl = absDl;
        this.rdTime = rdTime;
        this.utility = utility;
        this.relDl = relDl;
        this.priority = priority;
        this.miss = miss;
        this.occKind = occKind;
        this.boundDl = boundDl;
    }


    public String getAbsdl() {
        return absDl;
    }

    public void setAbsdl(String absDl) {
        this.absDl = absDl;
    }
    public String getRdtime() {
        return rdTime;
    }

    public void setRdtime(String rdTime) {
        this.rdTime = rdTime;
    }
    public String getUtility() {
        return utility;
    }

    public void setUtility(String utility) {
        this.utility = utility;
    }
    public String getReldl() {
        return relDl;
    }

    public void setReldl(String relDl) {
        this.relDl = relDl;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getMiss() {
        return miss;
    }

    public void setMiss(String miss) {
        this.miss = miss;
    }
    public String getOcckind() {
        return occKind;
    }

    public void setOcckind(String occKind) {
        this.occKind = occKind;
    }
    public String getBounddl() {
        return boundDl;
    }

    public void setBounddl(String boundDl) {
        this.boundDl = boundDl;
    }

    public HLAM_MARTE_BehavioralFeature getHlam_marte_behavioralfeature() {
        return hlam_marte_behavioralfeature;
    }

    public void setHlam_marte_behavioralfeature(HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature) {
        this.hlam_marte_behavioralfeature = hlam_marte_behavioralfeature;
    }

}