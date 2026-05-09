





import java.util.List;
import java.util.ArrayList;

public class ast_QualifiedName extends Name {






    private ast_Name ast_name;




    private ast_SimpleName ast_simplename;


    public ast_QualifiedName(
    ) {
        super(
        );
    }



    public ast_Name getAst_name() {
        return ast_name;
    }

    public void setAst_name(ast_Name ast_name) {
        this.ast_name = ast_name;
    }
    public ast_SimpleName getAst_simplename() {
        return ast_simplename;
    }

    public void setAst_simplename(ast_SimpleName ast_simplename) {
        this.ast_simplename = ast_simplename;
    }

}