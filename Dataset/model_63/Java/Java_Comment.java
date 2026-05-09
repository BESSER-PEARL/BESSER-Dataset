





import java.util.List;
import java.util.ArrayList;

public class Java_Comment extends ASTNode {

    private boolean prefixOfParent;
    private String content;
    private boolean enclosedByParent;





    private Java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private Java_AbstractTypeDeclaration java_abstracttypedeclaration;


    public Java_Comment(
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

    public Java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(Java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }
    public Java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(Java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }

}