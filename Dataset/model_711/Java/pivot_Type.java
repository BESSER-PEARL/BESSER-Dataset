





import java.util.List;
import java.util.ArrayList;

public class pivot_Type extends TemplateableElement, NamedElement, ParameterableElement {

    private String instanceClassName;





    private List<pivot_Operation> pivot_operations;




    private pivot_ElementExtension pivot_elementextension;




    private pivot_Package pivot_package;




    private pivot_Operation pivot_operation;




    private pivot_Operation pivot_operation;




    private List<pivot_Constraint> pivot_constraints;




    private pivot_Package pivot_package;




    private List<pivot_Type> pivot_types;


    public pivot_Type(
        String instanceClassName    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.pivot_operations = new ArrayList<>();
        this.pivot_constraints = new ArrayList<>();
        this.pivot_types = new ArrayList<>();
    }

    public pivot_Type(
        String instanceClassName        ArrayList<pivot_Operation> pivot_operations,        ArrayList<pivot_Constraint> pivot_constraints,        ArrayList<pivot_Type> pivot_types    ) {
        this.instanceClassName = instanceClassName;
        this.pivot_operations = pivot_operations;
        this.pivot_constraints = pivot_constraints;
        this.pivot_types = pivot_types;
    }

    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }
    public pivot_ElementExtension getPivot_elementextension() {
        return pivot_elementextension;
    }

    public void setPivot_elementextension(pivot_ElementExtension pivot_elementextension) {
        this.pivot_elementextension = pivot_elementextension;
    }
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public pivot_Package getPivot_package() {
        return pivot_package;
    }

    public void setPivot_package(pivot_Package pivot_package) {
        this.pivot_package = pivot_package;
    }
    public List<pivot_Type> getPivot_types() {
        return pivot_types;
    }

    public void addPivot_type(Pivot_type pivot_type) {
        this.pivot_types.add(pivot_type);
    }

}