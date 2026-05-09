





import java.util.List;
import java.util.ArrayList;

public class ast_ConditionalLoop extends LoopStatement {






    private ast_Expression ast_expression;


    public ast_ConditionalLoop(
    ) {
        super(
        );
    }



    public ast_Expression getAst_expression() {
        return ast_expression;
    }

    public void setAst_expression(ast_Expression ast_expression) {
        this.ast_expression = ast_expression;
    }

}