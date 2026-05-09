





import java.util.List;
import java.util.ArrayList;

public class analysis_bottlenecks_BottlenecksReport extends AnalysisReport {

    private String cpFirings;
    private float totalVariance;
    private float totalWeight;
    private float cpWeight;
    private float cpVariance;
    private String totalFirings;



    public analysis_bottlenecks_BottlenecksReport(
        String cpFirings,        float totalVariance,        float totalWeight,        float cpWeight,        float cpVariance,        String totalFirings    ) {
        super(
        );
        this.cpFirings = cpFirings;
        this.totalVariance = totalVariance;
        this.totalWeight = totalWeight;
        this.cpWeight = cpWeight;
        this.cpVariance = cpVariance;
        this.totalFirings = totalFirings;
    }


    public String getCpfirings() {
        return cpFirings;
    }

    public void setCpfirings(String cpFirings) {
        this.cpFirings = cpFirings;
    }
    public float getTotalvariance() {
        return totalVariance;
    }

    public void setTotalvariance(float totalVariance) {
        this.totalVariance = totalVariance;
    }
    public float getTotalweight() {
        return totalWeight;
    }

    public void setTotalweight(float totalWeight) {
        this.totalWeight = totalWeight;
    }
    public float getCpweight() {
        return cpWeight;
    }

    public void setCpweight(float cpWeight) {
        this.cpWeight = cpWeight;
    }
    public float getCpvariance() {
        return cpVariance;
    }

    public void setCpvariance(float cpVariance) {
        this.cpVariance = cpVariance;
    }
    public String getTotalfirings() {
        return totalFirings;
    }

    public void setTotalfirings(String totalFirings) {
        this.totalFirings = totalFirings;
    }


}