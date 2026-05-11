





import java.util.List;
import java.util.ArrayList;

public class VariableDeclaration  {






    private plsql_expression_SQLVariable plsql_expression_sqlvariable;




    private plsql_statement_ForStatement plsql_statement_forstatement;


    public VariableDeclaration(
    ) {
    }



    public plsql_expression_SQLVariable getPlsql_expression_sqlvariable() {
        return plsql_expression_sqlvariable;
    }

    public void setPlsql_expression_sqlvariable(plsql_expression_SQLVariable plsql_expression_sqlvariable) {
        this.plsql_expression_sqlvariable = plsql_expression_sqlvariable;
    }
    public plsql_statement_ForStatement getPlsql_statement_forstatement() {
        return plsql_statement_forstatement;
    }

    public void setPlsql_statement_forstatement(plsql_statement_ForStatement plsql_statement_forstatement) {
        this.plsql_statement_forstatement = plsql_statement_forstatement;
    }

}