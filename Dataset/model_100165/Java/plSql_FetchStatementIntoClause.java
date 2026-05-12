





import java.util.List;
import java.util.ArrayList;

public class plSql_FetchStatementIntoClause  {






    private List<plSql_VariableRef> plsql_variablerefs;




    private plSql_FetchStatement plsql_fetchstatement;


    public plSql_FetchStatementIntoClause(
    ) {
        this.plsql_variablerefs = new ArrayList<>();
    }

    public plSql_FetchStatementIntoClause(
        ArrayList<plSql_VariableRef> plsql_variablerefs    ) {
        this.plsql_variablerefs = plsql_variablerefs;
    }


    public List<plSql_VariableRef> getPlsql_variablerefs() {
        return plsql_variablerefs;
    }

    public void addPlsql_variableref(Plsql_variableref plsql_variableref) {
        this.plsql_variablerefs.add(plsql_variableref);
    }
    public plSql_FetchStatement getPlsql_fetchstatement() {
        return plsql_fetchstatement;
    }

    public void setPlsql_fetchstatement(plSql_FetchStatement plsql_fetchstatement) {
        this.plsql_fetchstatement = plsql_fetchstatement;
    }

}