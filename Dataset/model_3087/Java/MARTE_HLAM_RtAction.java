





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_RtAction  {

    private String isAtomic;
    private String synchKind;





    private HLAM_MARTE_InvocationAction hlam_marte_invocationaction;




    private HLAM_MARTE_BehavioralFeature hlam_marte_behavioralfeature;




    private NFP_DataSize nfp_datasize;


    public MARTE_HLAM_RtAction(
        String isAtomic,        String synchKind    ) {
        this.isAtomic = isAtomic;
        this.synchKind = synchKind;
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
    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }

}