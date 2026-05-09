





import java.util.List;
import java.util.ArrayList;

public class ast_ScopeStatement extends MethodContentStatement {






    private ast_MethodBlock ast_methodblock;


    public ast_ScopeStatement(
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