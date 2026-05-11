





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingStatistic  {

    private String totalRecords;
    private String message;





    private List<metrics_MappingRecord> metrics_mappingrecords;


    public metrics_MappingStatistic(
        String totalRecords,        String message    ) {
        this.totalRecords = totalRecords;
        this.message = message;
        this.metrics_mappingrecords = new ArrayList<>();
    }

    public metrics_MappingStatistic(
        String totalRecords,        String message        ArrayList<metrics_MappingRecord> metrics_mappingrecords    ) {
        this.totalRecords = totalRecords;
        this.message = message;
        this.metrics_mappingrecords = metrics_mappingrecords;
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

    public List<metrics_MappingRecord> getMetrics_mappingrecords() {
        return metrics_mappingrecords;
    }

    public void addMetrics_mappingrecord(Metrics_mappingrecord metrics_mappingrecord) {
        this.metrics_mappingrecords.add(metrics_mappingrecord);
    }

}