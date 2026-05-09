





import java.util.List;
import java.util.ArrayList;

public class java__TagElement extends ASTNode {

    private String tagName;





    private java__Javadoc java__javadoc;


    public java__TagElement(
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

    public java__Javadoc getJava__javadoc() {
        return java__javadoc;
    }

    public void setJava__javadoc(java__Javadoc java__javadoc) {
        this.java__javadoc = java__javadoc;
    }

}