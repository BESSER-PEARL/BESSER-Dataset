





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingStatistic extends Base {

    private String message;
    private String intervalEstimate;
    private String totalRecords;





    private List<metrics_MappingStatistic> metrics_mappingstatistics;




    private List<metrics_MappingRecord> metrics_mappingrecords;


    public metrics_MappingStatistic(
        String message,        String intervalEstimate,        String totalRecords    ) {
        super(
        );
        this.message = message;
        this.intervalEstimate = intervalEstimate;
        this.totalRecords = totalRecords;
        this.metrics_mappingstatistics = new ArrayList<>();
        this.metrics_mappingrecords = new ArrayList<>();
    }

    public metrics_MappingStatistic(
        String message,        String intervalEstimate,        String totalRecords        ArrayList<metrics_MappingStatistic> metrics_mappingstatistics,        ArrayList<metrics_MappingRecord> metrics_mappingrecords    ) {
        this.message = message;
        this.intervalEstimate = intervalEstimate;
        this.totalRecords = totalRecords;
        this.metrics_mappingstatistics = metrics_mappingstatistics;
        this.metrics_mappingrecords = metrics_mappingrecords;
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

    public List<metrics_MappingStatistic> getMetrics_mappingstatistics() {
        return metrics_mappingstatistics;
    }

    public void addMetrics_mappingstatistic(Metrics_mappingstatistic metrics_mappingstatistic) {
        this.metrics_mappingstatistics.add(metrics_mappingstatistic);
    }
    public List<metrics_MappingRecord> getMetrics_mappingrecords() {
        return metrics_mappingrecords;
    }

    public void addMetrics_mappingrecord(Metrics_mappingrecord metrics_mappingrecord) {
        this.metrics_mappingrecords.add(metrics_mappingrecord);
    }

}