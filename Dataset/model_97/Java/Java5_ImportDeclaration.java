





import java.util.List;
import java.util.ArrayList;

public class Java5_ImportDeclaration extends ASTNode {

    private boolean static;





    private Java5_CompilationUnit java5_compilationunit;




    private Java5_AbstractTypeDeclaration java5_abstracttypedeclaration;


    public Java5_ImportDeclaration(
        boolean static    ) {
        super(
        );
        this.static = static;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public Java5_CompilationUnit getJava5_compilationunit() {
        return java5_compilationunit;
    }

    public void setJava5_compilationunit(Java5_CompilationUnit java5_compilationunit) {
        this.java5_compilationunit = java5_compilationunit;
    }
    public Java5_AbstractTypeDeclaration getJava5_abstracttypedeclaration() {
        return java5_abstracttypedeclaration;
    }

    public void setJava5_abstracttypedeclaration(Java5_AbstractTypeDeclaration java5_abstracttypedeclaration) {
        this.java5_abstracttypedeclaration = java5_abstracttypedeclaration;
    }

}