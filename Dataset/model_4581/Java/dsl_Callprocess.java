





import java.util.List;
import java.util.ArrayList;

public class dsl_Callprocess extends Action {

    private String value;
    private String datasource;
    private String source;
    private String target;



    public dsl_Callprocess(
        String value,        String datasource,        String source,        String target    ) {
        super(
        );
        this.value = value;
        this.datasource = datasource;
        this.source = source;
        this.target = target;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getDatasource() {
        return datasource;
    }

    public void setDatasource(String datasource) {
        this.datasource = datasource;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}