





import java.util.List;
import java.util.ArrayList;

public class QualityMetrics_AggregatedRealMetric extends Metric {

    private float Median;
    private float Average;
    private float StandardDeviation;
    private float Minimum;
    private float Maximum;





    private QualityMetrics_Metrics qualitymetrics_metrics;


    public QualityMetrics_AggregatedRealMetric(
        float Median,        float Average,        float StandardDeviation,        float Minimum,        float Maximum    ) {
        super(
        );
        this.Median = Median;
        this.Average = Average;
        this.StandardDeviation = StandardDeviation;
        this.Minimum = Minimum;
        this.Maximum = Maximum;
    }


    public float getMedian() {
        return Median;
    }

    public void setMedian(float Median) {
        this.Median = Median;
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
    public float getMinimum() {
        return Minimum;
    }

    public void setMinimum(float Minimum) {
        this.Minimum = Minimum;
    }
    public float getMaximum() {
        return Maximum;
    }

    public void setMaximum(float Maximum) {
        this.Maximum = Maximum;
    }

    public QualityMetrics_Metrics getQualitymetrics_metrics() {
        return qualitymetrics_metrics;
    }

    public void setQualitymetrics_metrics(QualityMetrics_Metrics qualitymetrics_metrics) {
        this.qualitymetrics_metrics = qualitymetrics_metrics;
    }

}