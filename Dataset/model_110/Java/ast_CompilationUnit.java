





import java.util.List;
import java.util.ArrayList;

public class ast_CompilationUnit extends ASTNode {






    private List<ast_ImportDeclaration> ast_importdeclarations;


    public ast_CompilationUnit(
    ) {
        super(
        );
        this.ast_importdeclarations = new ArrayList<>();
    }

    public ast_CompilationUnit(
        ArrayList<ast_ImportDeclaration> ast_importdeclarations    ) {
        this.ast_importdeclarations = ast_importdeclarations;
    }


    public List<ast_ImportDeclaration> getAst_importdeclarations() {
        return ast_importdeclarations;
    }

    public void addAst_importdeclaration(Ast_importdeclaration ast_importdeclaration) {
        this.ast_importdeclarations.add(ast_importdeclaration);
    }

}