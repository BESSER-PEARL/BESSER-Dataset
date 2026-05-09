





import java.util.List;
import java.util.ArrayList;

public class ast_AnonymousClassDeclaration extends ASTNode {






    private ast_ClassInstanceCreation ast_classinstancecreation;


    public ast_AnonymousClassDeclaration(
    ) {
        super(
        );
    }



    public ast_ClassInstanceCreation getAst_classinstancecreation() {
        return ast_classinstancecreation;
    }

    public void setAst_classinstancecreation(ast_ClassInstanceCreation ast_classinstancecreation) {
        this.ast_classinstancecreation = ast_classinstancecreation;
    }

}