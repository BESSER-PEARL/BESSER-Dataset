





import java.util.List;
import java.util.ArrayList;

public class metrics_MappingXLSColumn  {

    private String column;





    private metrics_MappingXLS metrics_mappingxls;




    private metrics_DataKind metrics_datakind;


    public metrics_MappingXLSColumn(
        String column    ) {
        this.column = column;
    }


    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }

    public metrics_MappingXLS getMetrics_mappingxls() {
        return metrics_mappingxls;
    }

    public void setMetrics_mappingxls(metrics_MappingXLS metrics_mappingxls) {
        this.metrics_mappingxls = metrics_mappingxls;
    }
    public metrics_DataKind getMetrics_datakind() {
        return metrics_datakind;
    }

    public void setMetrics_datakind(metrics_DataKind metrics_datakind) {
        this.metrics_datakind = metrics_datakind;
    }

}