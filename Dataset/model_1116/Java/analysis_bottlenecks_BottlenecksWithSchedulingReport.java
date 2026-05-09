





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_BottlenecksWithSchedulingReport extends AnalysisReport, postprocessing_PostProcessingData {

    private String totalFirings;
    private float executionTime;
    private float cpBlockingTime;
    private String cpFirings;
    private float cpWeight;
    private float totalWeight;



    public analysis_bottlenecks_BottlenecksWithSchedulingReport(
        String totalFirings,        float executionTime,        float cpBlockingTime,        String cpFirings,        float cpWeight,        float totalWeight    ) {
        super(
        );
        this.totalFirings = totalFirings;
        this.executionTime = executionTime;
        this.cpBlockingTime = cpBlockingTime;
        this.cpFirings = cpFirings;
        this.cpWeight = cpWeight;
        this.totalWeight = totalWeight;
    }


    public String getTotalfirings() {
        return totalFirings;
    }

    public void setTotalfirings(String totalFirings) {
        this.totalFirings = totalFirings;
    }
    public float getExecutiontime() {
        return executionTime;
    }

    public void setExecutiontime(float executionTime) {
        this.executionTime = executionTime;
    }
    public float getCpblockingtime() {
        return cpBlockingTime;
    }

    public void setCpblockingtime(float cpBlockingTime) {
        this.cpBlockingTime = cpBlockingTime;
    }
    public String getCpfirings() {
        return cpFirings;
    }

    public void setCpfirings(String cpFirings) {
        this.cpFirings = cpFirings;
    }
    public float getCpweight() {
        return cpWeight;
    }

    public void setCpweight(float cpWeight) {
        this.cpWeight = cpWeight;
    }
    public float getTotalweight() {
        return totalWeight;
    }

    public void setTotalweight(float totalWeight) {
        this.totalWeight = totalWeight;
    }


}