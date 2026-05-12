





import java.util.List;
import java.util.ArrayList;

public class dbrouting_Executor extends ElementVisitor {

    private String executeBefore;
    private String statement;
    private String datasource;
    private String executeOnElementNS;
    private String executeOnElement;





    private dbrouting_DBRoutingDocumentRoot dbrouting_dbroutingdocumentroot;


    public dbrouting_Executor(
        String executeBefore,        String statement,        String datasource,        String executeOnElementNS,        String executeOnElement    ) {
        super(
        );
        this.executeBefore = executeBefore;
        this.statement = statement;
        this.datasource = datasource;
        this.executeOnElementNS = executeOnElementNS;
        this.executeOnElement = executeOnElement;
    }


    public String getExecutebefore() {
        return executeBefore;
    }

    public void setExecutebefore(String executeBefore) {
        this.executeBefore = executeBefore;
    }
    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }
    public String getDatasource() {
        return datasource;
    }

    public void setDatasource(String datasource) {
        this.datasource = datasource;
    }
    public String getExecuteonelementns() {
        return executeOnElementNS;
    }

    public void setExecuteonelementns(String executeOnElementNS) {
        this.executeOnElementNS = executeOnElementNS;
    }
    public String getExecuteonelement() {
        return executeOnElement;
    }

    public void setExecuteonelement(String executeOnElement) {
        this.executeOnElement = executeOnElement;
    }

    public dbrouting_DBRoutingDocumentRoot getDbrouting_dbroutingdocumentroot() {
        return dbrouting_dbroutingdocumentroot;
    }

    public void setDbrouting_dbroutingdocumentroot(dbrouting_DBRoutingDocumentRoot dbrouting_dbroutingdocumentroot) {
        this.dbrouting_dbroutingdocumentroot = dbrouting_dbroutingdocumentroot;
    }

}