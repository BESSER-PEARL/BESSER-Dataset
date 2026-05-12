





import java.util.List;
import java.util.ArrayList;

public class plSql_FetchStatement extends Statement {






    private plSql_VariableRef plsql_variableref;


    public plSql_FetchStatement(
    ) {
        super(
        );
    }



    public plSql_VariableRef getPlsql_variableref() {
        return plsql_variableref;
    }

    public void setPlsql_variableref(plSql_VariableRef plsql_variableref) {
        this.plsql_variableref = plsql_variableref;
    }

}