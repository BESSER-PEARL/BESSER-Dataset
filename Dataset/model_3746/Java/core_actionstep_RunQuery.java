





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_RunQuery extends actionstep_ActionStep, actionstep_Heavyweight {

    private String resultSetName;
    private boolean scrollable;
    private boolean readOnly;





    private DBResultSetId dbresultsetid;


    public core_actionstep_RunQuery(
        String resultSetName,        boolean scrollable,        boolean readOnly    ) {
        super(
        );
        this.resultSetName = resultSetName;
        this.scrollable = scrollable;
        this.readOnly = readOnly;
    }


    public String getResultsetname() {
        return resultSetName;
    }

    public void setResultsetname(String resultSetName) {
        this.resultSetName = resultSetName;
    }
    public boolean getScrollable() {
        return scrollable;
    }

    public void setScrollable(boolean scrollable) {
        this.scrollable = scrollable;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }

    public DBResultSetId getDbresultsetid() {
        return dbresultsetid;
    }

    public void setDbresultsetid(DBResultSetId dbresultsetid) {
        this.dbresultsetid = dbresultsetid;
    }

}