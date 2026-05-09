





import java.util.List;
import java.util.ArrayList;

public class javaMM_Comment extends ASTNode {

    private String content;
    private boolean prefixOfParent;
    private boolean enclosedByParent;





    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;


    public javaMM_Comment(
        String content,        boolean prefixOfParent,        boolean enclosedByParent    ) {
        super(
        );
        this.content = content;
        this.prefixOfParent = prefixOfParent;
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
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }

}