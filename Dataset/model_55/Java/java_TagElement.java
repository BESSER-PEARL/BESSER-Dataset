





import java.util.List;
import java.util.ArrayList;

public class java_TagElement extends ASTNode {

    private String tagName;



    public java_TagElement(
        String tagName    ) {
        super(
        );
        this.tagName = tagName;
    }


    public String getTagname() {
        return tagName;
    }

    public void setTagname(String tagName) {
        this.tagName = tagName;
    }


}