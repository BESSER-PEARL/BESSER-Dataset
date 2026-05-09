





import java.util.List;
import java.util.ArrayList;

public class ast_AbstractTypeDeclaration extends BodyDeclaration {






    private ast_CompilationUnit ast_compilationunit;




    private ast_TypeDeclarationStatement ast_typedeclarationstatement;


    public ast_AbstractTypeDeclaration(
    ) {
        super(
        );
    }



    public ast_CompilationUnit getAst_compilationunit() {
        return ast_compilationunit;
    }

    public void setAst_compilationunit(ast_CompilationUnit ast_compilationunit) {
        this.ast_compilationunit = ast_compilationunit;
    }
    public ast_TypeDeclarationStatement getAst_typedeclarationstatement() {
        return ast_typedeclarationstatement;
    }

    public void setAst_typedeclarationstatement(ast_TypeDeclarationStatement ast_typedeclarationstatement) {
        this.ast_typedeclarationstatement = ast_typedeclarationstatement;
    }

}