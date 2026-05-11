





import java.util.List;
import java.util.ArrayList;

public class metric_AggregatedRealMetric extends Metric {

    private float median;
    private float maximum;
    private float minimum;
    private float standardDeviation;
    private float average;



    public metric_AggregatedRealMetric(
        float median,        float maximum,        float minimum,        float standardDeviation,        float average    ) {
        super(
        );
        this.median = median;
        this.maximum = maximum;
        this.minimum = minimum;
        this.standardDeviation = standardDeviation;
        this.average = average;
    }


    public float getMedian() {
        return median;
    }

    public void setMedian(float median) {
        this.median = median;
    }
    public float getMaximum() {
        return maximum;
    }

    public void setMaximum(float maximum) {
        this.maximum = maximum;
    }
    public float getMinimum() {
        return minimum;
    }

    public void setMinimum(float minimum) {
        this.minimum = minimum;
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


}