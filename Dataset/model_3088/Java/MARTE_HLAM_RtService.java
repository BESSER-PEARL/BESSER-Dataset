





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_RtService  {

    private String synchKind;
    private String isAtomic;
    private String concPolicy;
    private String exeKind;





    private HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature;


    public MARTE_HLAM_RtService(
        String synchKind,        String isAtomic,        String concPolicy,        String exeKind    ) {
        this.synchKind = synchKind;
        this.isAtomic = isAtomic;
        this.concPolicy = concPolicy;
        this.exeKind = exeKind;
    }


    public String getSynchkind() {
        return synchKind;
    }

    public void setSynchkind(String synchKind) {
        this.synchKind = synchKind;
    }
    public String getIsatomic() {
        return isAtomic;
    }

    public void setIsatomic(String isAtomic) {
        this.isAtomic = isAtomic;
    }
    public String getConcpolicy() {
        return concPolicy;
    }

    public void setConcpolicy(String concPolicy) {
        this.concPolicy = concPolicy;
    }
    public String getExekind() {
        return exeKind;
    }

    public void setExekind(String exeKind) {
        this.exeKind = exeKind;
    }

    public HLAM_MARTE_BehavioralFeature getHlam_marte_behavioralfeature() {
        return hlam_marte_behavioralfeature;
    }

    public void setHlam_marte_behavioralfeature(HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature) {
        this.hlam_marte_behavioralfeature = hlam_marte_behavioralfeature;
    }

}