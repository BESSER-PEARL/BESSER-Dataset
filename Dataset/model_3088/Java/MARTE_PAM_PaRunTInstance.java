





import java.util.List;
import java.util.ArrayList;

public class MARTE_PAM_PaRunTInstance  {

    private String throughput;
    private String unbddPool;
    private String poolSize;
    private String utilization;





    private GRM_SchedulableResource grm_schedulableresource;




    private GQAM_GaExecHost gqam_gaexechost;


    public MARTE_PAM_PaRunTInstance(
        String throughput,        String unbddPool,        String poolSize,        String utilization    ) {
        this.throughput = throughput;
        this.unbddPool = unbddPool;
        this.poolSize = poolSize;
        this.utilization = utilization;
    }


    public String getThroughput() {
        return throughput;
    }

    public void setThroughput(String throughput) {
        this.throughput = throughput;
    }
    public String getUnbddpool() {
        return unbddPool;
    }

    public void setUnbddpool(String unbddPool) {
        this.unbddPool = unbddPool;
    }
    public String getPoolsize() {
        return poolSize;
    }

    public void setPoolsize(String poolSize) {
        this.poolSize = poolSize;
    }
    public String getUtilization() {
        return utilization;
    }

    public void setUtilization(String utilization) {
        this.utilization = utilization;
    }

    public GRM_SchedulableResource getGrm_schedulableresource() {
        return grm_schedulableresource;
    }

    public void setGrm_schedulableresource(GRM_SchedulableResource grm_schedulableresource) {
        this.grm_schedulableresource = grm_schedulableresource;
    }
    public GQAM_GaExecHost getGqam_gaexechost() {
        return gqam_gaexechost;
    }

    public void setGqam_gaexechost(GQAM_GaExecHost gqam_gaexechost) {
        this.gqam_gaexechost = gqam_gaexechost;
    }

}