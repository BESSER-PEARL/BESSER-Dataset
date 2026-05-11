





import java.util.List;
import java.util.ArrayList;

public class dsl_Updatedaudit extends Action {

    private String logsink;
    private String datasource;
    private String value;



    public dsl_Updatedaudit(
        String logsink,        String datasource,        String value    ) {
        super(
        );
        this.logsink = logsink;
        this.datasource = datasource;
        this.value = value;
    }


    public String getLogsink() {
        return logsink;
    }

    public void setLogsink(String logsink) {
        this.logsink = logsink;
    }
    public String getDatasource() {
        return datasource;
    }

    public void setDatasource(String datasource) {
        this.datasource = datasource;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}