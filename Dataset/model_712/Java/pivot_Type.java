





import java.util.List;
import java.util.ArrayList;

public class pivot_Type extends NamedElement, ParameterableElement, TemplateableElement {

    private String instanceClassName;





    private List<pivot_Constraint> pivot_constraints;




    private List<pivot_Type> pivot_types;


    public pivot_Type(
        String instanceClassName    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.pivot_constraints = new ArrayList<>();
        this.pivot_types = new ArrayList<>();
    }

    public pivot_Type(
        String instanceClassName        ArrayList<pivot_Constraint> pivot_constraints,        ArrayList<pivot_Type> pivot_types    ) {
        this.instanceClassName = instanceClassName;
        this.pivot_constraints = pivot_constraints;
        this.pivot_types = pivot_types;
    }

    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }

    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public List<pivot_Type> getPivot_types() {
        return pivot_types;
    }

    public void addPivot_type(Pivot_type pivot_type) {
        this.pivot_types.add(pivot_type);
    }

}