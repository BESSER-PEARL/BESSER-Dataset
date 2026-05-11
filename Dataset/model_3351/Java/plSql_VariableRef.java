





import java.util.List;
import java.util.ArrayList;

public class plSql_VariableRef  {

    private boolean isHostRef;





    private plSql_FetchStatement plsql_fetchstatement;




    private plSql_VariableAssignmentTarget plsql_variableassignmenttarget;




    private plSql_VariableRefExpression plsql_variablerefexpression;




    private plSql_CloseStatement plsql_closestatement;


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

    public plSql_FetchStatement getPlsql_fetchstatement() {
        return plsql_fetchstatement;
    }

    public void setPlsql_fetchstatement(plSql_FetchStatement plsql_fetchstatement) {
        this.plsql_fetchstatement = plsql_fetchstatement;
    }
    public plSql_VariableAssignmentTarget getPlsql_variableassignmenttarget() {
        return plsql_variableassignmenttarget;
    }

    public void setPlsql_variableassignmenttarget(plSql_VariableAssignmentTarget plsql_variableassignmenttarget) {
        this.plsql_variableassignmenttarget = plsql_variableassignmenttarget;
    }
    public plSql_VariableRefExpression getPlsql_variablerefexpression() {
        return plsql_variablerefexpression;
    }

    public void setPlsql_variablerefexpression(plSql_VariableRefExpression plsql_variablerefexpression) {
        this.plsql_variablerefexpression = plsql_variablerefexpression;
    }
    public plSql_CloseStatement getPlsql_closestatement() {
        return plsql_closestatement;
    }

    public void setPlsql_closestatement(plSql_CloseStatement plsql_closestatement) {
        this.plsql_closestatement = plsql_closestatement;
    }

}