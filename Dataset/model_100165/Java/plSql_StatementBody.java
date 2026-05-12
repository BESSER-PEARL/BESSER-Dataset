





import java.util.List;
import java.util.ArrayList;

public class plSql_StatementBody  {

    private String endName;





    private plSql_ProcedureImplementation plsql_procedureimplementation;


    public plSql_StatementBody(
        String endName    ) {
        this.endName = endName;
    }


    public String getEndname() {
        return endName;
    }

    public void setEndname(String endName) {
        this.endName = endName;
    }

    public plSql_ProcedureImplementation getPlsql_procedureimplementation() {
        return plsql_procedureimplementation;
    }

    public void setPlsql_procedureimplementation(plSql_ProcedureImplementation plsql_procedureimplementation) {
        this.plsql_procedureimplementation = plsql_procedureimplementation;
    }

}