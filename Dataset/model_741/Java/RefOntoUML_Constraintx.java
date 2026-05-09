





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Constraintx extends PackageableElement {






    private List<RefOntoUML_Element> refontouml_elements;


    public RefOntoUML_Constraintx(
    ) {
        super(
        );
        this.refontouml_elements = new ArrayList<>();
    }

    public RefOntoUML_Constraintx(
        ArrayList<RefOntoUML_Element> refontouml_elements    ) {
        this.refontouml_elements = refontouml_elements;
    }


    public List<RefOntoUML_Element> getRefontouml_elements() {
        return refontouml_elements;
    }

    public void addRefontouml_element(Refontouml_element refontouml_element) {
        this.refontouml_elements.add(refontouml_element);
    }

}