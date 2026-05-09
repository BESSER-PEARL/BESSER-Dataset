





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_AggregatedValueMetric extends ValueType {

    private String average;
    private String median;
    private String maximum;
    private String minimum;
    private String standardDeviation;



    public QualityMetamodel_AggregatedValueMetric(
        String average,        String median,        String maximum,        String minimum,        String standardDeviation    ) {
        super(
        );
        this.average = average;
        this.median = median;
        this.maximum = maximum;
        this.minimum = minimum;
        this.standardDeviation = standardDeviation;
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
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }
    public String getStandarddeviation() {
        return standardDeviation;
    }

    public void setStandarddeviation(String standardDeviation) {
        this.standardDeviation = standardDeviation;
    }


}