





import java.util.List;
import java.util.ArrayList;

public class QualityMetrics_AggregatedIntegerMetric extends Metric {

    private int Minimum;
    private float Average;
    private float StandardDeviation;
    private int Maximum;
    private int Median;





    private QualityMetrics_Metrics qualitymetrics_metrics;


    public QualityMetrics_AggregatedIntegerMetric(
        int Minimum,        float Average,        float StandardDeviation,        int Maximum,        int Median    ) {
        super(
        );
        this.Minimum = Minimum;
        this.Average = Average;
        this.StandardDeviation = StandardDeviation;
        this.Maximum = Maximum;
        this.Median = Median;
    }


    public int getMinimum() {
        return Minimum;
    }

    public void setMinimum(int Minimum) {
        this.Minimum = Minimum;
    }
    public float getAverage() {
        return Average;
    }

    public void setAverage(float Average) {
        this.Average = Average;
    }
    public float getStandarddeviation() {
        return StandardDeviation;
    }

    public void setStandarddeviation(float StandardDeviation) {
        this.StandardDeviation = StandardDeviation;
    }
    public int getMaximum() {
        return Maximum;
    }

    public void setMaximum(int Maximum) {
        this.Maximum = Maximum;
    }
    public int getMedian() {
        return Median;
    }

    public void setMedian(int Median) {
        this.Median = Median;
    }

    public QualityMetrics_Metrics getQualitymetrics_metrics() {
        return qualitymetrics_metrics;
    }

    public void setQualitymetrics_metrics(QualityMetrics_Metrics qualitymetrics_metrics) {
        this.qualitymetrics_metrics = qualitymetrics_metrics;
    }

}