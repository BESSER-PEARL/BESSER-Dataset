





import java.util.List;
import java.util.ArrayList;

public class UMLModel_RedefinableElement extends NamedElement {

    private String redefinedElement;
    private String isLeaf;
    private String redefinitionContext;



    public UMLModel_RedefinableElement(
        String redefinedElement,        String isLeaf,        String redefinitionContext    ) {
        super(
        );
        this.redefinedElement = redefinedElement;
        this.isLeaf = isLeaf;
        this.redefinitionContext = redefinitionContext;
    }


    public String getRedefinedelement() {
        return redefinedElement;
    }

    public void setRedefinedelement(String redefinedElement) {
        this.redefinedElement = redefinedElement;
    }
    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }
    public String getRedefinitioncontext() {
        return redefinitionContext;
    }

    public void setRedefinitioncontext(String redefinitionContext) {
        this.redefinitionContext = redefinitionContext;
    }


}