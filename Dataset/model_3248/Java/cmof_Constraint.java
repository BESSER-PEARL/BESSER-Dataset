





import java.util.List;
import java.util.ArrayList;

public class cmof_Constraint extends PackageableElement {






    private cmof_ValueSpecification cmof_valuespecification;




    private List<cmof_Element> cmof_elements;




    private cmof_Operation cmof_operation;




    private cmof_Operation cmof_operation;




    private cmof_Operation cmof_operation;




    private cmof_Namespace cmof_namespace;




    private cmof_Namespace cmof_namespace;


    public cmof_Constraint(
    ) {
        super(
        );
        this.cmof_elements = new ArrayList<>();
    }

    public cmof_Constraint(
        ArrayList<cmof_Element> cmof_elements    ) {
        this.cmof_elements = cmof_elements;
    }


    public cmof_ValueSpecification getCmof_valuespecification() {
        return cmof_valuespecification;
    }

    public void setCmof_valuespecification(cmof_ValueSpecification cmof_valuespecification) {
        this.cmof_valuespecification = cmof_valuespecification;
    }
    public List<cmof_Element> getCmof_elements() {
        return cmof_elements;
    }

    public void addCmof_element(Cmof_element cmof_element) {
        this.cmof_elements.add(cmof_element);
    }
    public cmof_Operation getCmof_operation() {
        return cmof_operation;
    }

    public void setCmof_operation(cmof_Operation cmof_operation) {
        this.cmof_operation = cmof_operation;
    }
    public cmof_Operation getCmof_operation() {
        return cmof_operation;
    }

    public void setCmof_operation(cmof_Operation cmof_operation) {
        this.cmof_operation = cmof_operation;
    }
    public cmof_Operation getCmof_operation() {
        return cmof_operation;
    }

    public void setCmof_operation(cmof_Operation cmof_operation) {
        this.cmof_operation = cmof_operation;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }

}