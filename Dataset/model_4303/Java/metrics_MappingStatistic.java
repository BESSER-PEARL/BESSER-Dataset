





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingStatistic extends Base {

    private String intervalEstimate;
    private String message;
    private String totalRecords;





    private List<metrics_MappingRecord> metrics_mappingrecords;




    private metrics_MappingStatistic metrics_mappingstatistic;




    private metrics_MetricSource metrics_metricsource;


    public metrics_MappingStatistic(
        String intervalEstimate,        String message,        String totalRecords    ) {
        super(
        );
        this.intervalEstimate = intervalEstimate;
        this.message = message;
        this.totalRecords = totalRecords;
        this.metrics_mappingrecords = new ArrayList<>();
    }

    public metrics_MappingStatistic(
        String intervalEstimate,        String message,        String totalRecords        ArrayList<metrics_MappingRecord> metrics_mappingrecords    ) {
        this.intervalEstimate = intervalEstimate;
        this.message = message;
        this.totalRecords = totalRecords;
        this.metrics_mappingrecords = metrics_mappingrecords;
    }

    public String getIntervalestimate() {
        return intervalEstimate;
    }

    public void setIntervalestimate(String intervalEstimate) {
        this.intervalEstimate = intervalEstimate;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getTotalrecords() {
        return totalRecords;
    }

    public void setTotalrecords(String totalRecords) {
        this.totalRecords = totalRecords;
    }

    public List<metrics_MappingRecord> getMetrics_mappingrecords() {
        return metrics_mappingrecords;
    }

    public void addMetrics_mappingrecord(Metrics_mappingrecord metrics_mappingrecord) {
        this.metrics_mappingrecords.add(metrics_mappingrecord);
    }
    public metrics_MappingStatistic getMetrics_mappingstatistic() {
        return metrics_mappingstatistic;
    }

    public void setMetrics_mappingstatistic(metrics_MappingStatistic metrics_mappingstatistic) {
        this.metrics_mappingstatistic = metrics_mappingstatistic;
    }
    public metrics_MetricSource getMetrics_metricsource() {
        return metrics_metricsource;
    }

    public void setMetrics_metricsource(metrics_MetricSource metrics_metricsource) {
        this.metrics_metricsource = metrics_metricsource;
    }

}