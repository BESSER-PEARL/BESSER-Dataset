





import java.util.List;
import java.util.ArrayList;

public class ast_BreakStatement extends Statement {






    private ast_SimpleName ast_simplename;


    public ast_BreakStatement(
    ) {
        super(
        );
    }



    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}