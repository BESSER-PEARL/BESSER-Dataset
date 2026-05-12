





import java.util.List;
import java.util.ArrayList;

public class plSql_FunctionImplementation extends FunctionContent {






    private plSql_StatementBody plsql_statementbody;




    private plSql_DeclareSection plsql_declaresection;


    public plSql_FunctionImplementation(
    ) {
        super(
        );
    }



    public plSql_StatementBody getPlsql_statementbody() {
        return plsql_statementbody;
    }

    public void setPlsql_statementbody(plSql_StatementBody plsql_statementbody) {
        this.plsql_statementbody = plsql_statementbody;
    }
    public plSql_DeclareSection getPlsql_declaresection() {
        return plsql_declaresection;
    }

    public void setPlsql_declaresection(plSql_DeclareSection plsql_declaresection) {
        this.plsql_declaresection = plsql_declaresection;
    }

}