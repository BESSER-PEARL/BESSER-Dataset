





import java.util.List;
import java.util.ArrayList;

public class JDTAST_TagElement extends ASTNode {

    private String tagName;
    private String nested;



    public JDTAST_TagElement(
        String tagName,        String nested    ) {
        super(
        );
        this.tagName = tagName;
        this.nested = nested;
    }


    public String getTagname() {
        return tagName;
    }

    public void setTagname(String tagName) {
        this.tagName = tagName;
    }
    public String getNested() {
        return nested;
    }

    public void setNested(String nested) {
        this.nested = nested;
    }


}