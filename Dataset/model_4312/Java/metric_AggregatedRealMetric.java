





import java.util.List;
import java.util.ArrayList;

public class metric_AggregatedRealMetric extends Metric {

    private float maximum;
    private float average;
    private float median;
    private float minimum;
    private float standardDeviation;



    public metric_AggregatedRealMetric(
        float maximum,        float average,        float median,        float minimum,        float standardDeviation    ) {
        super(
        );
        this.maximum = maximum;
        this.average = average;
        this.median = median;
        this.minimum = minimum;
        this.standardDeviation = standardDeviation;
    }


    public float getMaximum() {
        return maximum;
    }

    public void setMaximum(float maximum) {
        this.maximum = maximum;
    }
    public float getAverage() {
        return average;
    }

    public void setAverage(float average) {
        this.average = average;
    }
    public float getMedian() {
        return median;
    }

    public void setMedian(float median) {
        this.median = median;
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


}