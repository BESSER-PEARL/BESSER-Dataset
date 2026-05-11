





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingColumn extends Base {

    private String column;





    private metrics_Mapping metrics_mapping;




    private metrics_Mapping metrics_mapping;




    private metrics_DataKind metrics_datakind;


    public metrics_MappingColumn(
        String column    ) {
        super(
        );
        this.column = column;
    }


    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }

    public metrics_Mapping getMetrics_mapping() {
        return metrics_mapping;
    }

    public void setMetrics_mapping(metrics_Mapping metrics_mapping) {
        this.metrics_mapping = metrics_mapping;
    }
    public metrics_Mapping getMetrics_mapping() {
        return metrics_mapping;
    }

    public void setMetrics_mapping(metrics_Mapping metrics_mapping) {
        this.metrics_mapping = metrics_mapping;
    }
    public metrics_DataKind getMetrics_datakind() {
        return metrics_datakind;
    }

    public void setMetrics_datakind(metrics_DataKind metrics_datakind) {
        this.metrics_datakind = metrics_datakind;
    }

}