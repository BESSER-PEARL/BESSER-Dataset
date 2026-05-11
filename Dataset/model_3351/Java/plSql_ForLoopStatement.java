





import java.util.List;
import java.util.ArrayList;

public class plSql_ForLoopStatement extends LoopStatement {






    private plSql_Expression plsql_expression;




    private plSql_LoopVariableDeclaration plsql_loopvariabledeclaration;




    private plSql_Expression plsql_expression;


    public plSql_ForLoopStatement(
    ) {
        super(
        );
    }



    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }
    public plSql_LoopVariableDeclaration getPlsql_loopvariabledeclaration() {
        return plsql_loopvariabledeclaration;
    }

    public void setPlsql_loopvariabledeclaration(plSql_LoopVariableDeclaration plsql_loopvariabledeclaration) {
        this.plsql_loopvariabledeclaration = plsql_loopvariabledeclaration;
    }
    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }

}