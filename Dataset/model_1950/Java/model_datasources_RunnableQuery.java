





import java.util.List;
import java.util.ArrayList;

public class model_datasources_RunnableQuery  {

    private String booleanOperator;
    private String queryPath;
    private String targetVariablePath;



    public model_datasources_RunnableQuery(
        String booleanOperator,        String queryPath,        String targetVariablePath    ) {
        this.booleanOperator = booleanOperator;
        this.queryPath = queryPath;
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
    public String getTargetvariablepath() {
        return targetVariablePath;
    }

    public void setTargetvariablepath(String targetVariablePath) {
        this.targetVariablePath = targetVariablePath;
    }


}