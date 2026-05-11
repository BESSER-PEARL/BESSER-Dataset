





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_RtAction  {

    private String synchKind;
    private String isAtomic;
    private String msgSize;





    private HLAM_MARTE_InvocationAction hlam_marte_invocationaction;




    private HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature;


    public MARTE_HLAM_RtAction(
        String synchKind,        String isAtomic,        String msgSize    ) {
        this.synchKind = synchKind;
        this.isAtomic = isAtomic;
        this.msgSize = msgSize;
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
    public String getMsgsize() {
        return msgSize;
    }

    public void setMsgsize(String msgSize) {
        this.msgSize = msgSize;
    }

    public HLAM_MARTE_InvocationAction getHlam_marte_invocationaction() {
        return hlam_marte_invocationaction;
    }

    public void setHlam_marte_invocationaction(HLAM_MARTE_InvocationAction hlam_marte_invocationaction) {
        this.hlam_marte_invocationaction = hlam_marte_invocationaction;
    }
    public HLAM_MARTE_BehavioralFeature getHlam_marte_behavioralfeature() {
        return hlam_marte_behavioralfeature;
    }

    public void setHlam_marte_behavioralfeature(HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature) {
        this.hlam_marte_behavioralfeature = hlam_marte_behavioralfeature;
    }

}