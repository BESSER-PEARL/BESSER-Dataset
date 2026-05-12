





import java.util.List;
import java.util.ArrayList;

public class plSql_VariableValue  {






    private plSql_Expression plsql_expression;




    private plSql_VariableDeclaration plsql_variabledeclaration;


    public plSql_VariableValue(
    ) {
    }



    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }
    public plSql_VariableDeclaration getPlsql_variabledeclaration() {
        return plsql_variabledeclaration;
    }

    public void setPlsql_variabledeclaration(plSql_VariableDeclaration plsql_variabledeclaration) {
        this.plsql_variabledeclaration = plsql_variabledeclaration;
    }

}