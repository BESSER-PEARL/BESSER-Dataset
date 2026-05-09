





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_AggregatedValueMetric extends ValueType {

    private String maximum;
    private String standardDeviation;
    private String minimum;
    private String average;
    private String median;



    public QualityMetamodel_AggregatedValueMetric(
        String maximum,        String standardDeviation,        String minimum,        String average,        String median    ) {
        super(
        );
        this.maximum = maximum;
        this.standardDeviation = standardDeviation;
        this.minimum = minimum;
        this.average = average;
        this.median = median;
    }


    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getStandarddeviation() {
        return standardDeviation;
    }

    public void setStandarddeviation(String standardDeviation) {
        this.standardDeviation = standardDeviation;
    }
    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }
    public String getAverage() {
        return average;
    }

    public void setAverage(String average) {
        this.average = average;
    }
    public String getMedian() {
        return median;
    }

    public void setMedian(String median) {
        this.median = median;
    }


}