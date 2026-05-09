





import java.util.List;
import java.util.ArrayList;

public class ast_NewOp extends Expression {






    private ast_ArrayConstructor ast_arrayconstructor;


    public ast_NewOp(
    ) {
        super(
        );
    }



    public ast_ArrayConstructor getAst_arrayconstructor() {
        return ast_arrayconstructor;
    }

    public void setAst_arrayconstructor(ast_ArrayConstructor ast_arrayconstructor) {
        this.ast_arrayconstructor = ast_arrayconstructor;
    }

}