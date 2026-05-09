





import java.util.List;
import java.util.ArrayList;

public class javaMM_Comment extends ASTNode {

    private boolean enclosedByParent;
    private String content;
    private boolean prefixOfParent;





    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;


    public javaMM_Comment(
        boolean enclosedByParent,        String content,        boolean prefixOfParent    ) {
        super(
        );
        this.enclosedByParent = enclosedByParent;
        this.content = content;
        this.prefixOfParent = prefixOfParent;
    }


    public boolean getEnclosedbyparent() {
        return enclosedByParent;
    }

    public void setEnclosedbyparent(boolean enclosedByParent) {
        this.enclosedByParent = enclosedByParent;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public boolean getPrefixofparent() {
        return prefixOfParent;
    }

    public void setPrefixofparent(boolean prefixOfParent) {
        this.prefixOfParent = prefixOfParent;
    }

    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }

}