





import java.util.List;
import java.util.ArrayList;

public class metric_AggregatedIntegerMetric extends Metric {

    private String median;
    private float average;
    private float standardDeviation;
    private String maximum;
    private String minimum;



    public metric_AggregatedIntegerMetric(
        String median,        float average,        float standardDeviation,        String maximum,        String minimum    ) {
        super(
        );
        this.median = median;
        this.average = average;
        this.standardDeviation = standardDeviation;
        this.maximum = maximum;
        this.minimum = minimum;
    }


    public String getMedian() {
        return median;
    }

    public void setMedian(String median) {
        this.median = median;
    }
    public float getAverage() {
        return average;
    }

    public void setAverage(float average) {
        this.average = average;
    }
    public float getStandarddeviation() {
        return standardDeviation;
    }

    public void setStandarddeviation(float standardDeviation) {
        this.standardDeviation = standardDeviation;
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


}