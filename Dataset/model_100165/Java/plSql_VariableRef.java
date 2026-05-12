





import java.util.List;
import java.util.ArrayList;

public class plSql_VariableRef  {

    private boolean isHostRef;





    private plSql_VariableRefExpression plsql_variablerefexpression;


    public plSql_VariableRef(
        boolean isHostRef    ) {
        this.isHostRef = isHostRef;
    }


    public boolean getIshostref() {
        return isHostRef;
    }

    public void setIshostref(boolean isHostRef) {
        this.isHostRef = isHostRef;
    }

    public plSql_VariableRefExpression getPlsql_variablerefexpression() {
        return plsql_variablerefexpression;
    }

    public void setPlsql_variablerefexpression(plSql_VariableRefExpression plsql_variablerefexpression) {
        this.plsql_variablerefexpression = plsql_variablerefexpression;
    }

}