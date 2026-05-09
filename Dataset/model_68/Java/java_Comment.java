





import java.util.List;
import java.util.ArrayList;

public class java_Comment extends ASTNode {

    private boolean enclosedByParent;
    private boolean prefixOfParent;
    private String content;



    public java_Comment(
        boolean enclosedByParent,        boolean prefixOfParent,        String content    ) {
        super(
        );
        this.enclosedByParent = enclosedByParent;
        this.prefixOfParent = prefixOfParent;
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
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}