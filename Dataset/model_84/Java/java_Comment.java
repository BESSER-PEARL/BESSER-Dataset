





import java.util.List;
import java.util.ArrayList;

public class java_Comment extends ASTNode {

    private String content;
    private boolean enclosedByParent;
    private boolean prefixOfParent;





    private java_CompilationUnit java_compilationunit;


    public java_Comment(
        String content,        boolean enclosedByParent,        boolean prefixOfParent    ) {
        super(
        );
        this.content = content;
        this.enclosedByParent = enclosedByParent;
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
    public boolean getPrefixofparent() {
        return prefixOfParent;
    }

    public void setPrefixofparent(boolean prefixOfParent) {
        this.prefixOfParent = prefixOfParent;
    }

    public java_CompilationUnit getJava_compilationunit() {
        return java_compilationunit;
    }

    public void setJava_compilationunit(java_CompilationUnit java_compilationunit) {
        this.java_compilationunit = java_compilationunit;
    }

}