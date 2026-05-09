





import java.util.List;
import java.util.ArrayList;

public class java_Comment extends ASTNode {

    private boolean prefixOfParent;
    private boolean enclosedByParent;
    private String content;



    public java_Comment(
        boolean prefixOfParent,        boolean enclosedByParent,        String content    ) {
        super(
        );
        this.prefixOfParent = prefixOfParent;
        this.enclosedByParent = enclosedByParent;
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
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}