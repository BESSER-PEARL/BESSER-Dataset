





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_RtService  {

    private String concPolicy;
    private String exeKind;
    private String isAtomic;
    private String synchKind;





    private HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature;


    public MARTE_HLAM_RtService(
        String concPolicy,        String exeKind,        String isAtomic,        String synchKind    ) {
        this.concPolicy = concPolicy;
        this.exeKind = exeKind;
        this.isAtomic = isAtomic;
        this.synchKind = synchKind;
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
    public String getIsatomic() {
        return isAtomic;
    }

    public void setIsatomic(String isAtomic) {
        this.isAtomic = isAtomic;
    }
    public String getSynchkind() {
        return synchKind;
    }

    public void setSynchkind(String synchKind) {
        this.synchKind = synchKind;
    }

    public HLAM_MARTE_BehavioralFeature getHlam_marte_behavioralfeature() {
        return hlam_marte_behavioralfeature;
    }

    public void setHlam_marte_behavioralfeature(HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature) {
        this.hlam_marte_behavioralfeature = hlam_marte_behavioralfeature;
    }

}