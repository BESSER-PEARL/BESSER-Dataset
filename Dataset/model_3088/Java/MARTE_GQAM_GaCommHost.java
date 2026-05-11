





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaCommHost extends GRM_Scheduler, GRM_CommunicationMedia {

    private String throughput;
    private String utilization;



    public MARTE_GQAM_GaCommHost(
        String throughput,        String utilization    ) {
        super(
        );
        this.throughput = throughput;
        this.utilization = utilization;
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


}