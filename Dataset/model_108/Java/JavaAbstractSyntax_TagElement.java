





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_TagElement extends ASTNode {

    private String nested;
    private String tagName;



    public JavaAbstractSyntax_TagElement(
        String nested,        String tagName    ) {
        super(
        );
        this.nested = nested;
        this.tagName = tagName;
    }


    public String getNested() {
        return nested;
    }

    public void setNested(String nested) {
        this.nested = nested;
    }
    public String getTagname() {
        return tagName;
    }

    public void setTagname(String tagName) {
        this.tagName = tagName;
    }


}