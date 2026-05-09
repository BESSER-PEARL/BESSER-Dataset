





import java.util.List;
import java.util.ArrayList;

public class ast_LoopStatement extends LabeledStatement {






    private ast_MethodBlock ast_methodblock;


    public ast_LoopStatement(
    ) {
        super(
        );
    }



    public ast_MethodBlock getAst_methodblock() {
        return ast_methodblock;
    }

    public void setAst_methodblock(ast_MethodBlock ast_methodblock) {
        this.ast_methodblock = ast_methodblock;
    }

}