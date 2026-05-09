





import java.util.List;
import java.util.ArrayList;

public class RefUML_Constraintx extends PackageableElement {






    private RefUML_ValueSpecification refuml_valuespecification;




    private List<RefUML_Element> refuml_elements;


    public RefUML_Constraintx(
    ) {
        super(
        );
        this.refuml_elements = new ArrayList<>();
    }

    public RefUML_Constraintx(
        ArrayList<RefUML_Element> refuml_elements    ) {
        this.refuml_elements = refuml_elements;
    }


    public RefUML_ValueSpecification getRefuml_valuespecification() {
        return refuml_valuespecification;
    }

    public void setRefuml_valuespecification(RefUML_ValueSpecification refuml_valuespecification) {
        this.refuml_valuespecification = refuml_valuespecification;
    }
    public List<RefUML_Element> getRefuml_elements() {
        return refuml_elements;
    }

    public void addRefuml_element(Refuml_element refuml_element) {
        this.refuml_elements.add(refuml_element);
    }

}