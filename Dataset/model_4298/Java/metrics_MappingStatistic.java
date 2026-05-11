





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingStatistic  {

    private String totalRecords;





    private List<metrics_MappingRecord> metrics_mappingrecords;


    public metrics_MappingStatistic(
        String totalRecords    ) {
        this.totalRecords = totalRecords;
        this.metrics_mappingrecords = new ArrayList<>();
    }

    public metrics_MappingStatistic(
        String totalRecords        ArrayList<metrics_MappingRecord> metrics_mappingrecords    ) {
        this.totalRecords = totalRecords;
        this.metrics_mappingrecords = metrics_mappingrecords;
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

}