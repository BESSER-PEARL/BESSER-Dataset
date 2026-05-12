





import java.util.List;
import java.util.ArrayList;

public class plSql_ProcedureInvokerRightsClause  {

    private String right;





    private plSql_Package plsql_package;




    private plSql_Procedure plsql_procedure;


    public plSql_ProcedureInvokerRightsClause(
        String right    ) {
        this.right = right;
    }


    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }

    public plSql_Package getPlsql_package() {
        return plsql_package;
    }

    public void setPlsql_package(plSql_Package plsql_package) {
        this.plsql_package = plsql_package;
    }
    public plSql_Procedure getPlsql_procedure() {
        return plsql_procedure;
    }

    public void setPlsql_procedure(plSql_Procedure plsql_procedure) {
        this.plsql_procedure = plsql_procedure;
    }

}