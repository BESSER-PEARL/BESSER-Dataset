





import java.util.List;
import java.util.ArrayList;

public class ast_ArrayInitializer extends Expression {






    private ast_ArrayCreation ast_arraycreation;


    public ast_ArrayInitializer(
    ) {
        super(
        );
    }



    public ast_ArrayCreation getAst_arraycreation() {
        return ast_arraycreation;
    }

    public void setAst_arraycreation(ast_ArrayCreation ast_arraycreation) {
        this.ast_arraycreation = ast_arraycreation;
    }

}