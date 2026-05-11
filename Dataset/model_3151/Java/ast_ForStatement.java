





import java.util.List;
import java.util.ArrayList;

public class ast_ForStatement extends Statement {






    private ast_IterationVariable ast_iterationvariable;




    private ast_Expression ast_expression;


    public ast_ForStatement(
    ) {
        super(
        );
    }



    public ast_IterationVariable getAst_iterationvariable() {
        return ast_iterationvariable;
    }

    public void setAst_iterationvariable(ast_IterationVariable ast_iterationvariable) {
        this.ast_iterationvariable = ast_iterationvariable;
    }
    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}