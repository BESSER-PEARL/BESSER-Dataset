





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingStatistic extends Base {

    private String totalRecords;
    private String message;
    private String intervalEstimate;





    private List<metrics_MappingStatistic> metrics_mappingstatistics;


    public metrics_MappingStatistic(
        String totalRecords,        String message,        String intervalEstimate    ) {
        super(
        );
        this.totalRecords = totalRecords;
        this.message = message;
        this.intervalEstimate = intervalEstimate;
        this.metrics_mappingstatistics = new ArrayList<>();
    }

    public metrics_MappingStatistic(
        String totalRecords,        String message,        String intervalEstimate        ArrayList<metrics_MappingStatistic> metrics_mappingstatistics    ) {
        this.totalRecords = totalRecords;
        this.message = message;
        this.intervalEstimate = intervalEstimate;
        this.metrics_mappingstatistics = metrics_mappingstatistics;
    }

    public String getTotalrecords() {
        return totalRecords;
    }

    public void setTotalrecords(String totalRecords) {
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

    public List<metrics_MappingStatistic> getMetrics_mappingstatistics() {
        return metrics_mappingstatistics;
    }

    public void addMetrics_mappingstatistic(Metrics_mappingstatistic metrics_mappingstatistic) {
        this.metrics_mappingstatistics.add(metrics_mappingstatistic);
    }

}