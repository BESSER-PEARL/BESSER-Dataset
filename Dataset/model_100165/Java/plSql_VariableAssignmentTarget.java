





import java.util.List;
import java.util.ArrayList;

public class plSql_VariableAssignmentTarget extends AssignmentTarget {






    private plSql_VariableRef plsql_variableref;


    public plSql_VariableAssignmentTarget(
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