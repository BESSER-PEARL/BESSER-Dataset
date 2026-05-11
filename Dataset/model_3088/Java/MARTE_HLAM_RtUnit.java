





import java.util.List;
import java.util.ArrayList;

public class MARTE_HLAM_RtUnit  {

    private String srPoolPolicy;
    private String srPoolSize;
    private String msgMaxSize;
    private String isDynamic;
    private String queueSize;
    private String queueSchedPolicy;
    private String isMain;
    private String memorySize;
    private String srPoolWaitingTime;





    private HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier;


    public MARTE_HLAM_RtUnit(
        String srPoolPolicy,        String srPoolSize,        String msgMaxSize,        String isDynamic,        String queueSize,        String queueSchedPolicy,        String isMain,        String memorySize,        String srPoolWaitingTime    ) {
        this.srPoolPolicy = srPoolPolicy;
        this.srPoolSize = srPoolSize;
        this.msgMaxSize = msgMaxSize;
        this.isDynamic = isDynamic;
        this.queueSize = queueSize;
        this.queueSchedPolicy = queueSchedPolicy;
        this.isMain = isMain;
        this.memorySize = memorySize;
        this.srPoolWaitingTime = srPoolWaitingTime;
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
    public String getMsgmaxsize() {
        return msgMaxSize;
    }

    public void setMsgmaxsize(String msgMaxSize) {
        this.msgMaxSize = msgMaxSize;
    }
    public String getIsdynamic() {
        return isDynamic;
    }

    public void setIsdynamic(String isDynamic) {
        this.isDynamic = isDynamic;
    }
    public String getQueuesize() {
        return queueSize;
    }

    public void setQueuesize(String queueSize) {
        this.queueSize = queueSize;
    }
    public String getQueueschedpolicy() {
        return queueSchedPolicy;
    }

    public void setQueueschedpolicy(String queueSchedPolicy) {
        this.queueSchedPolicy = queueSchedPolicy;
    }
    public String getIsmain() {
        return isMain;
    }

    public void setIsmain(String isMain) {
        this.isMain = isMain;
    }
    public String getMemorysize() {
        return memorySize;
    }

    public void setMemorysize(String memorySize) {
        this.memorySize = memorySize;
    }
    public String getSrpoolwaitingtime() {
        return srPoolWaitingTime;
    }

    public void setSrpoolwaitingtime(String srPoolWaitingTime) {
        this.srPoolWaitingTime = srPoolWaitingTime;
    }

    public HLAM_MARTE_BehavioredClassifier getHlam_marte_behavioredclassifier() {
        return hlam_marte_behavioredclassifier;
    }

    public void setHlam_marte_behavioredclassifier(HLAM_MARTE_BehavioredClassifier hlam_marte_behavioredclassifier) {
        this.hlam_marte_behavioredclassifier = hlam_marte_behavioredclassifier;
    }

}