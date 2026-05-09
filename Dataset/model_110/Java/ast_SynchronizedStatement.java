





import java.util.List;
import java.util.ArrayList;

public class ast_SynchronizedStatement extends Statement {






    private ast_Expression ast_expression;




    private ast_Block ast_block;


    public ast_SynchronizedStatement(
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
    public ast_Block getAst_block() {
        return ast_block;
    }

    public void setAst_block(ast_Block ast_block) {
        this.ast_block = ast_block;
    }

}