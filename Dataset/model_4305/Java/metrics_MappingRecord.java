





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingRecord extends Base {

    private String column;
    private String message;
    private String count;





    private metrics_MappingStatistic metrics_mappingstatistic;


    public metrics_MappingRecord(
        String column,        String message,        String count    ) {
        super(
        );
        this.column = column;
        this.message = message;
        this.count = count;
    }


    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
    }

    public metrics_MappingStatistic getMetrics_mappingstatistic() {
        return metrics_mappingstatistic;
    }

    public void setMetrics_mappingstatistic(metrics_MappingStatistic metrics_mappingstatistic) {
        this.metrics_mappingstatistic = metrics_mappingstatistic;
    }

}