





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_ActionBottlenecksWithSchedulingData  {

    private float cpWeight;
    private String totalFirings;
    private String cpFirings;
    private float totalWeight;





    private bottlenecks_analysis_Action bottlenecks_analysis_action;


    public analysis_bottlenecks_ActionBottlenecksWithSchedulingData(
        float cpWeight,        String totalFirings,        String cpFirings,        float totalWeight    ) {
        this.cpWeight = cpWeight;
        this.totalFirings = totalFirings;
        this.cpFirings = cpFirings;
        this.totalWeight = totalWeight;
    }


    public float getCpweight() {
        return cpWeight;
    }

    public void setCpweight(float cpWeight) {
        this.cpWeight = cpWeight;
    }
    public String getTotalfirings() {
        return totalFirings;
    }

    public void setTotalfirings(String totalFirings) {
        this.totalFirings = totalFirings;
    }
    public String getCpfirings() {
        return cpFirings;
    }

    public void setCpfirings(String cpFirings) {
        this.cpFirings = cpFirings;
    }
    public float getTotalweight() {
        return totalWeight;
    }

    public void setTotalweight(float totalWeight) {
        this.totalWeight = totalWeight;
    }

    public bottlenecks_analysis_Action getBottlenecks_analysis_action() {
        return bottlenecks_analysis_action;
    }

    public void setBottlenecks_analysis_action(bottlenecks_analysis_Action bottlenecks_analysis_action) {
        this.bottlenecks_analysis_action = bottlenecks_analysis_action;
    }

}