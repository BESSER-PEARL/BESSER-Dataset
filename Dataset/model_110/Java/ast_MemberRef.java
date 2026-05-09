





import java.util.List;
import java.util.ArrayList;

public class ast_MemberRef extends ASTNode, IDocElement {






    private ast_Name ast_name;


    public ast_MemberRef(
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

}