





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_GetColValue extends ActionStep {

    private String getAsDatatype;





    private DBResultSetId dbresultsetid;


    public core_actionstep_GetColValue(
        String getAsDatatype    ) {
        super(
        );
        this.getAsDatatype = getAsDatatype;
    }


    public String getGetasdatatype() {
        return getAsDatatype;
    }

    public void setGetasdatatype(String getAsDatatype) {
        this.getAsDatatype = getAsDatatype;
    }

    public DBResultSetId getDbresultsetid() {
        return dbresultsetid;
    }

    public void setDbresultsetid(DBResultSetId dbresultsetid) {
        this.dbresultsetid = dbresultsetid;
    }

}