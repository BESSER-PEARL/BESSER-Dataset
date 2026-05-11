





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaExecHost extends GRM_Scheduler, GRM_ComputingResource {

    private String commRcvOvh;
    private String commTxOvh;
    private String schedPriRange;
    private String utilization;
    private String clockOvh;
    private String cntxtSwT;
    private String memSize;
    private String throughput;



    public MARTE_GQAM_GaExecHost(
        String commRcvOvh,        String commTxOvh,        String schedPriRange,        String utilization,        String clockOvh,        String cntxtSwT,        String memSize,        String throughput    ) {
        super(
        );
        this.commRcvOvh = commRcvOvh;
        this.commTxOvh = commTxOvh;
        this.schedPriRange = schedPriRange;
        this.utilization = utilization;
        this.clockOvh = clockOvh;
        this.cntxtSwT = cntxtSwT;
        this.memSize = memSize;
        this.throughput = throughput;
    }


    public String getCommrcvovh() {
        return commRcvOvh;
    }

    public void setCommrcvovh(String commRcvOvh) {
        this.commRcvOvh = commRcvOvh;
    }
    public String getCommtxovh() {
        return commTxOvh;
    }

    public void setCommtxovh(String commTxOvh) {
        this.commTxOvh = commTxOvh;
    }
    public String getSchedprirange() {
        return schedPriRange;
    }

    public void setSchedprirange(String schedPriRange) {
        this.schedPriRange = schedPriRange;
    }
    public String getUtilization() {
        return utilization;
    }

    public void setUtilization(String utilization) {
        this.utilization = utilization;
    }
    public String getClockovh() {
        return clockOvh;
    }

    public void setClockovh(String clockOvh) {
        this.clockOvh = clockOvh;
    }
    public String getCntxtswt() {
        return cntxtSwT;
    }

    public void setCntxtswt(String cntxtSwT) {
        this.cntxtSwT = cntxtSwT;
    }
    public String getMemsize() {
        return memSize;
    }

    public void setMemsize(String memSize) {
        this.memSize = memSize;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }


}