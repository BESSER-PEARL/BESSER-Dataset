





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_ActionBottlenecksData  {

    private float cpWeight;
    private float slackMax;
    private float cpVariance;
    private float totalVariance;
    private float slackMin;
    private String totalFirings;
    private float totalWeight;
    private String cpFirings;





    private bottlenecks_analysis_Action bottlenecks_analysis_action;


    public analysis_bottlenecks_ActionBottlenecksData(
        float cpWeight,        float slackMax,        float cpVariance,        float totalVariance,        float slackMin,        String totalFirings,        float totalWeight,        String cpFirings    ) {
        this.cpWeight = cpWeight;
        this.slackMax = slackMax;
        this.cpVariance = cpVariance;
        this.totalVariance = totalVariance;
        this.slackMin = slackMin;
        this.totalFirings = totalFirings;
        this.totalWeight = totalWeight;
        this.cpFirings = cpFirings;
    }


    public float getCpweight() {
        return cpWeight;
    }

    public void setCpweight(float cpWeight) {
        this.cpWeight = cpWeight;
    }
    public float getSlackmax() {
        return slackMax;
    }

    public void setSlackmax(float slackMax) {
        this.slackMax = slackMax;
    }
    public float getCpvariance() {
        return cpVariance;
    }

    public void setCpvariance(float cpVariance) {
        this.cpVariance = cpVariance;
    }
    public float getTotalvariance() {
        return totalVariance;
    }

    public void setTotalvariance(float totalVariance) {
        this.totalVariance = totalVariance;
    }
    public float getSlackmin() {
        return slackMin;
    }

    public void setSlackmin(float slackMin) {
        this.slackMin = slackMin;
    }
    public String getTotalfirings() {
        return totalFirings;
    }

    public void setTotalfirings(String totalFirings) {
        this.totalFirings = totalFirings;
    }
    public float getTotalweight() {
        return totalWeight;
    }

    public void setTotalweight(float totalWeight) {
        this.totalWeight = totalWeight;
    }
    public String getCpfirings() {
        return cpFirings;
    }

    public void setCpfirings(String cpFirings) {
        this.cpFirings = cpFirings;
    }

    public bottlenecks_analysis_Action getBottlenecks_analysis_action() {
        return bottlenecks_analysis_action;
    }

    public void setBottlenecks_analysis_action(bottlenecks_analysis_Action bottlenecks_analysis_action) {
        this.bottlenecks_analysis_action = bottlenecks_analysis_action;
    }

}