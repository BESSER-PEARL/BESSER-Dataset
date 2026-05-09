





import java.util.List;
import java.util.ArrayList;

public class java__Comment extends ASTNode {

    private String content;
    private boolean prefixOfParent;
    private boolean enclosedByParent;



    public java__Comment(
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


}