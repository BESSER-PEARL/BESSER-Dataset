





import java.util.List;
import java.util.ArrayList;

public class model_datasources_RunnableQuery  {

    private String targetVariablePath;
    private String booleanOperator;
    private String queryPath;



    public model_datasources_RunnableQuery(
        String targetVariablePath,        String booleanOperator,        String queryPath    ) {
        this.targetVariablePath = targetVariablePath;
        this.booleanOperator = booleanOperator;
        this.queryPath = queryPath;
    }


    public String getTargetvariablepath() {
        return targetVariablePath;
    }

    public void setTargetvariablepath(String targetVariablePath) {
        this.targetVariablePath = targetVariablePath;
    }
    public String getBooleanoperator() {
        return booleanOperator;
    }

    public void setBooleanoperator(String booleanOperator) {
        this.booleanOperator = booleanOperator;
    }
    public String getQuerypath() {
        return queryPath;
    }

    public void setQuerypath(String queryPath) {
        this.queryPath = queryPath;
    }


}