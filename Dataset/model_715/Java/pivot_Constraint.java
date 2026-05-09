





import java.util.List;
import java.util.ArrayList;

public class pivot_Constraint extends NamedElement {

    private String isCallable;





    private List<pivot_Constraint> pivot_constraints;




    private pivot_Namespace pivot_namespace;




    private pivot_Namespace pivot_namespace;


    public pivot_Constraint(
        String isCallable    ) {
        super(
        );
        this.isCallable = isCallable;
        this.pivot_constraints = new ArrayList<>();
    }

    public pivot_Constraint(
        String isCallable        ArrayList<pivot_Constraint> pivot_constraints    ) {
        this.isCallable = isCallable;
        this.pivot_constraints = pivot_constraints;
    }

    public String getIscallable() {
        return isCallable;
    }

    public void setIscallable(String isCallable) {
        this.isCallable = isCallable;
    }

    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public pivot_Namespace getPivot_namespace() {
        return pivot_namespace;
    }

    public void setPivot_namespace(pivot_Namespace pivot_namespace) {
        this.pivot_namespace = pivot_namespace;
    }
    public pivot_Namespace getPivot_namespace() {
        return pivot_namespace;
    }

    public void setPivot_namespace(pivot_Namespace pivot_namespace) {
        this.pivot_namespace = pivot_namespace;
    }

}