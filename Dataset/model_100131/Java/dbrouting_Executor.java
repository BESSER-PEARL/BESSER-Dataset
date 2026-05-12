





import java.util.List;
import java.util.ArrayList;

public class dbrouting_Executor extends ElementVisitor {

    private String executeOnElementNS;
    private String statement;
    private String executeBefore;
    private String datasource;
    private String executeOnElement;



    public dbrouting_Executor(
        String executeOnElementNS,        String statement,        String executeBefore,        String datasource,        String executeOnElement    ) {
        super(
        );
        this.executeOnElementNS = executeOnElementNS;
        this.statement = statement;
        this.executeBefore = executeBefore;
        this.datasource = datasource;
        this.executeOnElement = executeOnElement;
    }


    public String getExecuteonelementns() {
        return executeOnElementNS;
    }

    public void setExecuteonelementns(String executeOnElementNS) {
        this.executeOnElementNS = executeOnElementNS;
    }
    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }
    public String getExecutebefore() {
        return executeBefore;
    }

    public void setExecutebefore(String executeBefore) {
        this.executeBefore = executeBefore;
    }
    public String getDatasource() {
        return datasource;
    }

    public void setDatasource(String datasource) {
        this.datasource = datasource;
    }
    public String getExecuteonelement() {
        return executeOnElement;
    }

    public void setExecuteonelement(String executeOnElement) {
        this.executeOnElement = executeOnElement;
    }


}