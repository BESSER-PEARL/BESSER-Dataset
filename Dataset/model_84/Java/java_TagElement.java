





import java.util.List;
import java.util.ArrayList;

public class java_TagElement extends ASTNode {

    private String tagName;





    private java_Javadoc java_javadoc;


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

    public java_Javadoc getJava_javadoc() {
        return java_javadoc;
    }

    public void setJava_javadoc(java_Javadoc java_javadoc) {
        this.java_javadoc = java_javadoc;
    }

}