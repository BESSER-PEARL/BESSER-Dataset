





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingStatistic extends Base {

    private String message;
    private String intervalEstimate;
    private String totalRecords;





    private metrics_MetricSource metrics_metricsource;


    public metrics_MappingStatistic(
        String message,        String intervalEstimate,        String totalRecords    ) {
        super(
        );
        this.message = message;
        this.intervalEstimate = intervalEstimate;
        this.totalRecords = totalRecords;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getIntervalestimate() {
        return intervalEstimate;
    }

    public void setIntervalestimate(String intervalEstimate) {
        this.intervalEstimate = intervalEstimate;
    }
    public String getTotalrecords() {
        return totalRecords;
    }

    public void setTotalrecords(String totalRecords) {
        this.totalRecords = totalRecords;
    }

    public metrics_MetricSource getMetrics_metricsource() {
        return metrics_metricsource;
    }

    public void setMetrics_metricsource(metrics_MetricSource metrics_metricsource) {
        this.metrics_metricsource = metrics_metricsource;
    }

}