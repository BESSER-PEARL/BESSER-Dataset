





import java.util.List;
import java.util.ArrayList;

public class javaMM_Comment extends ASTNode {

    private boolean prefixOfParent;
    private String content;
    private boolean enclosedByParent;





    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_CompilationUnit javamm_compilationunit;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;


    public javaMM_Comment(
        boolean prefixOfParent,        String content,        boolean enclosedByParent    ) {
        super(
        );
        this.prefixOfParent = prefixOfParent;
        this.content = content;
        this.enclosedByParent = enclosedByParent;
    }


    public boolean getPrefixofparent() {
        return prefixOfParent;
    }

    public void setPrefixofparent(boolean prefixOfParent) {
        this.prefixOfParent = prefixOfParent;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public boolean getEnclosedbyparent() {
        return enclosedByParent;
    }

    public void setEnclosedbyparent(boolean enclosedByParent) {
        this.enclosedByParent = enclosedByParent;
    }

    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public javaMM_CompilationUnit getJavamm_compilationunit() {
        return javamm_compilationunit;
    }

    public void setJavamm_compilationunit(javaMM_CompilationUnit javamm_compilationunit) {
        this.javamm_compilationunit = javamm_compilationunit;
    }
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }

}