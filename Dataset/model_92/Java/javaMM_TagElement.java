





import java.util.List;
import java.util.ArrayList;

public class javaMM_TagElement extends ASTNode {

    private String tagName;





    private javaMM_Javadoc javamm_javadoc;


    public javaMM_TagElement(
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

    public javaMM_Javadoc getJavamm_javadoc() {
        return javamm_javadoc;
    }

    public void setJavamm_javadoc(javaMM_Javadoc javamm_javadoc) {
        this.javamm_javadoc = javamm_javadoc;
    }

}