





import java.util.List;
import java.util.ArrayList;

public class java_Comment extends ASTNode {

    private boolean enclosedByParent;
    private String content;
    private boolean prefixOfParent;





    private java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private java_AbstractTypeDeclaration java_abstracttypedeclaration;


    public java_Comment(
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

    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }
    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }

}