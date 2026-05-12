





import java.util.List;
import java.util.ArrayList;

public class dbrouting_ResultSetRowSelector extends ElementVisitor {

    private String failedSelectError;
    private String resultSetName;
    private String where;
    private String executeBefore;
    private String beanId;
    private String selectRowOnElement;





    private dbrouting_DocumentRoot dbrouting_documentroot;


    public dbrouting_ResultSetRowSelector(
        String failedSelectError,        String resultSetName,        String where,        String executeBefore,        String beanId,        String selectRowOnElement    ) {
        super(
        );
        this.failedSelectError = failedSelectError;
        this.resultSetName = resultSetName;
        this.where = where;
        this.executeBefore = executeBefore;
        this.beanId = beanId;
        this.selectRowOnElement = selectRowOnElement;
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
    public String getWhere() {
        return where;
    }

    public void setWhere(String where) {
        this.where = where;
    }
    public String getExecutebefore() {
        return executeBefore;
    }

    public void setExecutebefore(String executeBefore) {
        this.executeBefore = executeBefore;
    }
    public String getBeanid() {
        return beanId;
    }

    public void setBeanid(String beanId) {
        this.beanId = beanId;
    }
    public String getSelectrowonelement() {
        return selectRowOnElement;
    }

    public void setSelectrowonelement(String selectRowOnElement) {
        this.selectRowOnElement = selectRowOnElement;
    }

    public dbrouting_DocumentRoot getDbrouting_documentroot() {
        return dbrouting_documentroot;
    }

    public void setDbrouting_documentroot(dbrouting_DocumentRoot dbrouting_documentroot) {
        this.dbrouting_documentroot = dbrouting_documentroot;
    }

}