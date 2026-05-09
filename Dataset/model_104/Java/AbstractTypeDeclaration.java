





import java.util.List;
import java.util.ArrayList;

public class AbstractTypeDeclaration  {






    private DOM_CompilationUnit dom_compilationunit;




    private DOM_TypeDeclarationStatement dom_typedeclarationstatement;


    public AbstractTypeDeclaration(
    ) {
    }



    public DOM_CompilationUnit getDom_compilationunit() {
        return dom_compilationunit;
    }

    public void setDom_compilationunit(DOM_CompilationUnit dom_compilationunit) {
        this.dom_compilationunit = dom_compilationunit;
    }
    public DOM_TypeDeclarationStatement getDom_typedeclarationstatement() {
        return dom_typedeclarationstatement;
    }

    public void setDom_typedeclarationstatement(DOM_TypeDeclarationStatement dom_typedeclarationstatement) {
        this.dom_typedeclarationstatement = dom_typedeclarationstatement;
    }

}