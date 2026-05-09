





import java.util.List;
import java.util.ArrayList;

public class analysis_partitioning_BalancedPipelinePartition  {

    private float preWorkload;
    private float commonPredAvg;
    private float workload;



    public analysis_partitioning_BalancedPipelinePartition(
        float preWorkload,        float commonPredAvg,        float workload    ) {
        this.preWorkload = preWorkload;
        this.commonPredAvg = commonPredAvg;
        this.workload = workload;
    }


    public float getPreworkload() {
        return preWorkload;
    }

    public void setPreworkload(float preWorkload) {
        this.preWorkload = preWorkload;
    }
    public float getCommonpredavg() {
        return commonPredAvg;
    }

    public void setCommonpredavg(float commonPredAvg) {
        this.commonPredAvg = commonPredAvg;
    }
    public float getWorkload() {
        return workload;
    }

    public void setWorkload(float workload) {
        this.workload = workload;
    }


}