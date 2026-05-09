





import java.util.List;
import java.util.ArrayList;

public class uml_RedefinableElement extends NamedElement {

    private String isLeaf;



    public uml_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
    }


    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }


}