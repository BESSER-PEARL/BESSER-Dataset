





import java.util.List;
import java.util.ArrayList;

public class ast_InitStatement extends ClassifierMemberStatement {






    private ast_MethodBlock ast_methodblock;


    public ast_InitStatement(
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