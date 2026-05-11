





import java.util.List;
import java.util.ArrayList;

public class MARTE_PAM_PaLogicalResource extends Resource {

    private String utilization;
    private String poolSize;
    private String throughput;



    public MARTE_PAM_PaLogicalResource(
        String utilization,        String poolSize,        String throughput    ) {
        super(
        );
        this.utilization = utilization;
        this.poolSize = poolSize;
        this.throughput = throughput;
    }


    public String getUtilization() {
        return utilization;
    }

    public void setUtilization(String utilization) {
        this.utilization = utilization;
    }
    public String getPoolsize() {
        return poolSize;
    }

    public void setPoolsize(String poolSize) {
        this.poolSize = poolSize;
    }
    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }


}