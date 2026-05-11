





import java.util.List;
import java.util.ArrayList;

public class QualityMetrics_SimpleMetric extends Metric {

    private int Value;





    private QualityMetrics_Metrics qualitymetrics_metrics;


    public QualityMetrics_SimpleMetric(
        int Value    ) {
        super(
        );
        this.Value = Value;
    }


    public int getValue() {
        return Value;
    }

    public void setValue(int Value) {
        this.Value = Value;
    }

    public QualityMetrics_Metrics getQualitymetrics_metrics() {
        return qualitymetrics_metrics;
    }

    public void setQualitymetrics_metrics(QualityMetrics_Metrics qualitymetrics_metrics) {
        this.qualitymetrics_metrics = qualitymetrics_metrics;
    }

}