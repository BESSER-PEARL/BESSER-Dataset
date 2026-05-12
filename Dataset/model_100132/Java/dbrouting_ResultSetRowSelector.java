





import java.util.List;
import java.util.ArrayList;

public class dbrouting_ResultSetRowSelector extends ElementVisitor {

    private String beanId;
    private String where;
    private String failedSelectError;
    private String resultSetName;
    private String executeBefore;
    private String selectRowOnElement;





    private dbrouting_DBRoutingDocumentRoot dbrouting_dbroutingdocumentroot;


    public dbrouting_ResultSetRowSelector(
        String beanId,        String where,        String failedSelectError,        String resultSetName,        String executeBefore,        String selectRowOnElement    ) {
        super(
        );
        this.beanId = beanId;
        this.where = where;
        this.failedSelectError = failedSelectError;
        this.resultSetName = resultSetName;
        this.executeBefore = executeBefore;
        this.selectRowOnElement = selectRowOnElement;
    }


    public String getBeanid() {
        return beanId;
    }

    public void setBeanid(String beanId) {
        this.beanId = beanId;
    }
    public String getWhere() {
        return where;
    }

    public void setWhere(String where) {
        this.where = where;
    }
    public String getFailedselecterror() {
        return failedSelectError;
    }

    public void setFailedselecterror(String failedSelectError) {
        this.failedSelectError = failedSelectError;
    }
    public String getResultsetname() {
        return resultSetName;
    }

    public void setResultsetname(String resultSetName) {
        this.resultSetName = resultSetName;
    }
    public String getExecutebefore() {
        return executeBefore;
    }

    public void setExecutebefore(String executeBefore) {
        this.executeBefore = executeBefore;
    }
    public String getSelectrowonelement() {
        return selectRowOnElement;
    }

    public void setSelectrowonelement(String selectRowOnElement) {
        this.selectRowOnElement = selectRowOnElement;
    }

    public dbrouting_DBRoutingDocumentRoot getDbrouting_dbroutingdocumentroot() {
        return dbrouting_dbroutingdocumentroot;
    }

    public void setDbrouting_dbroutingdocumentroot(dbrouting_DBRoutingDocumentRoot dbrouting_dbroutingdocumentroot) {
        this.dbrouting_dbroutingdocumentroot = dbrouting_dbroutingdocumentroot;
    }

}