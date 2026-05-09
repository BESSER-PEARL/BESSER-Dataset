





import java.util.List;
import java.util.ArrayList;

public class ast_ClassBlock extends EJBase {






    private ast_NewOp ast_newop;


    public ast_ClassBlock(
    ) {
        super(
        );
    }



    public ast_NewOp getAst_newop() {
        return ast_newop;
    }

    public void setAst_newop(ast_NewOp ast_newop) {
        this.ast_newop = ast_newop;
    }

}