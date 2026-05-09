





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Constraintx extends PackageableElement {






    private RefOntoUML_ValueSpecification refontouml_valuespecification;




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


    public RefOntoUML_ValueSpecification getRefontouml_valuespecification() {
        return refontouml_valuespecification;
    }

    public void setRefontouml_valuespecification(RefOntoUML_ValueSpecification refontouml_valuespecification) {
        this.refontouml_valuespecification = refontouml_valuespecification;
    }
    public List<RefOntoUML_Element> getRefontouml_elements() {
        return refontouml_elements;
    }

    public void addRefontouml_element(Refontouml_element refontouml_element) {
        this.refontouml_elements.add(refontouml_element);
    }

}