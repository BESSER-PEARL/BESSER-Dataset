





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_RtUnit  {

    private String queueSchedPolicy;
    private String queueSize;
    private String srPoolPolicy;
    private String srPoolSize;
    private String isMain;
    private String isDynamic;





    private NFP_DataSize nfp_datasize;




    private NFP_DataSize nfp_datasize;




    private NFP_Duration nfp_duration;




    private HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier;


    public MARTE_HLAM_RtUnit(
        String queueSchedPolicy,        String queueSize,        String srPoolPolicy,        String srPoolSize,        String isMain,        String isDynamic    ) {
        this.queueSchedPolicy = queueSchedPolicy;
        this.queueSize = queueSize;
        this.srPoolPolicy = srPoolPolicy;
        this.srPoolSize = srPoolSize;
        this.isMain = isMain;
        this.isDynamic = isDynamic;
    }


    public String getQueueschedpolicy() {
        return queueSchedPolicy;
    }

    public void setQueueschedpolicy(String queueSchedPolicy) {
        this.queueSchedPolicy = queueSchedPolicy;
    }
    public String getQueuesize() {
        return queueSize;
    }

    public void setQueuesize(String queueSize) {
        this.queueSize = queueSize;
    }
    public String getSrpoolpolicy() {
        return srPoolPolicy;
    }

    public void setSrpoolpolicy(String srPoolPolicy) {
        this.srPoolPolicy = srPoolPolicy;
    }
    public String getSrpoolsize() {
        return srPoolSize;
    }

    public void setSrpoolsize(String srPoolSize) {
        this.srPoolSize = srPoolSize;
    }
    public String getIsmain() {
        return isMain;
    }

    public void setIsmain(String isMain) {
        this.isMain = isMain;
    }
    public String getIsdynamic() {
        return isDynamic;
    }

    public void setIsdynamic(String isDynamic) {
        this.isDynamic = isDynamic;
    }

    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }
    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }
    public NFP_Duration getNfp_duration() {
        return nfp_duration;
    }

    public void setNfp_duration(NFP_Duration nfp_duration) {
        this.nfp_duration = nfp_duration;
    }
    public HLAM_MARTE_BehavioredClassifier getHlam_marte_behavioredclassifier() {
        return hlam_marte_behavioredclassifier;
    }

    public void setHlam_marte_behavioredclassifier(HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier) {
        this.hlam_marte_behavioredclassifier = hlam_marte_behavioredclassifier;
    }

}