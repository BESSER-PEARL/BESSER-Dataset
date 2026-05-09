





import java.util.List;
import java.util.ArrayList;

public class pivot_Constraint extends NamedElement {

    private String isCallable;





    private pivot_Namespace pivot_namespace;




    private pivot_Operation pivot_operation;




    private pivot_Type pivot_type;




    private List<pivot_Element> pivot_elements;




    private pivot_OpaqueExpression pivot_opaqueexpression;




    private List<pivot_Constraint> pivot_constraints;




    private pivot_Operation pivot_operation;




    private pivot_Namespace pivot_namespace;


    public pivot_Constraint(
        String isCallable    ) {
        super(
        );
        this.isCallable = isCallable;
        this.pivot_elements = new ArrayList<>();
        this.pivot_constraints = new ArrayList<>();
    }

    public pivot_Constraint(
        String isCallable        ArrayList<pivot_Element> pivot_elements,        ArrayList<pivot_Constraint> pivot_constraints    ) {
        this.isCallable = isCallable;
        this.pivot_elements = pivot_elements;
        this.pivot_constraints = pivot_constraints;
    }

    public String getIscallable() {
        return isCallable;
    }

    public void setIscallable(String isCallable) {
        this.isCallable = isCallable;
    }

    public pivot_Namespace getPivot_namespace() {
        return pivot_namespace;
    }

    public void setPivot_namespace(pivot_Namespace pivot_namespace) {
        this.pivot_namespace = pivot_namespace;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public List<pivot_Element> getPivot_elements() {
        return pivot_elements;
    }

    public void addPivot_element(Pivot_element pivot_element) {
        this.pivot_elements.add(pivot_element);
    }
    public pivot_OpaqueExpression getPivot_opaqueexpression() {
        return pivot_opaqueexpression;
    }

    public void setPivot_opaqueexpression(pivot_OpaqueExpression pivot_opaqueexpression) {
        this.pivot_opaqueexpression = pivot_opaqueexpression;
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Namespace getPivot_namespace() {
        return pivot_namespace;
    }

    public void setPivot_namespace(pivot_Namespace pivot_namespace) {
        this.pivot_namespace = pivot_namespace;
    }

}