





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaScenario extends GRM_ResourceUsage, Time_TimedProcessing {

    private String respT;
    private String throughput;
    private String utilization;
    private String utilizationOnHost;
    private String hostDemandOps;
    private String interOccT;
    private String hostDemand;



    public MARTE_GQAM_GaScenario(
        String respT,        String throughput,        String utilization,        String utilizationOnHost,        String hostDemandOps,        String interOccT,        String hostDemand    ) {
        super(
        );
        this.respT = respT;
        this.throughput = throughput;
        this.utilization = utilization;
        this.utilizationOnHost = utilizationOnHost;
        this.hostDemandOps = hostDemandOps;
        this.interOccT = interOccT;
        this.hostDemand = hostDemand;
    }


    public String getRespt() {
        return respT;
    }

    public void setRespt(String respT) {
        this.respT = respT;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getUtilization() {
        return utilization;
    }

    public void setUtilization(String utilization) {
        this.utilization = utilization;
    }
    public String getUtilizationonhost() {
        return utilizationOnHost;
    }

    public void setUtilizationonhost(String utilizationOnHost) {
        this.utilizationOnHost = utilizationOnHost;
    }
    public String getHostdemandops() {
        return hostDemandOps;
    }

    public void setHostdemandops(String hostDemandOps) {
        this.hostDemandOps = hostDemandOps;
    }
    public String getInterocct() {
        return interOccT;
    }

    public void setInterocct(String interOccT) {
        this.interOccT = interOccT;
    }
    public String getHostdemand() {
        return hostDemand;
    }

    public void setHostdemand(String hostDemand) {
        this.hostDemand = hostDemand;
    }


}