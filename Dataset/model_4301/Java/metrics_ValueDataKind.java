





import java.util.List;
import java.util.ArrayList;

public class metrics_ValueDataKind extends DataKind {

    private String kindHint;
    private String valueKind;
    private String format;





    private metrics_Metric metrics_metric;


    public metrics_ValueDataKind(
        String kindHint,        String valueKind,        String format    ) {
        super(
        );
        this.kindHint = kindHint;
        this.valueKind = valueKind;
        this.format = format;
    }


    public String getKindhint() {
        return kindHint;
    }

    public void setKindhint(String kindHint) {
        this.kindHint = kindHint;
    }
    public String getValuekind() {
        return valueKind;
    }

    public void setValuekind(String valueKind) {
        this.valueKind = valueKind;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public metrics_Metric getMetrics_metric() {
        return metrics_metric;
    }

    public void setMetrics_metric(metrics_Metric metrics_metric) {
        this.metrics_metric = metrics_metric;
    }

}