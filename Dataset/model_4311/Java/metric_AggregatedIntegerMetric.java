





import java.util.List;
import java.util.ArrayList;

public class metric_AggregatedIntegerMetric extends Metric {

    private String minimum;
    private String maximum;
    private float standardDeviation;
    private float average;
    private String median;



    public metric_AggregatedIntegerMetric(
        String minimum,        String maximum,        float standardDeviation,        float average,        String median    ) {
        super(
        );
        this.minimum = minimum;
        this.maximum = maximum;
        this.standardDeviation = standardDeviation;
        this.average = average;
        this.median = median;
    }


    public String getMinimum() {
        return minimum;
    }

    public void setMinimum(String minimum) {
        this.minimum = minimum;
    }
    public String getMaximum() {
        return maximum;
    }

    public void setMaximum(String maximum) {
        this.maximum = maximum;
    }
    public float getStandarddeviation() {
        return standardDeviation;
    }

    public void setStandarddeviation(float standardDeviation) {
        this.standardDeviation = standardDeviation;
    }
    public float getAverage() {
        return average;
    }

    public void setAverage(float average) {
        this.average = average;
    }
    public String getMedian() {
        return median;
    }

    public void setMedian(String median) {
        this.median = median;
    }


}