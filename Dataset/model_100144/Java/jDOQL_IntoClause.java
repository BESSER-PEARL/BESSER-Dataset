





import java.util.List;
import java.util.ArrayList;

public class jDOQL_IntoClause  {

    private String resultClassName;





    private jDOQL_SelectClause jdoql_selectclause;


    public jDOQL_IntoClause(
        String resultClassName    ) {
        this.resultClassName = resultClassName;
    }


    public String getResultclassname() {
        return resultClassName;
    }

    public void setResultclassname(String resultClassName) {
        this.resultClassName = resultClassName;
    }

    public jDOQL_SelectClause getJdoql_selectclause() {
        return jdoql_selectclause;
    }

    public void setJdoql_selectclause(jDOQL_SelectClause jdoql_selectclause) {
        this.jdoql_selectclause = jdoql_selectclause;
    }

}