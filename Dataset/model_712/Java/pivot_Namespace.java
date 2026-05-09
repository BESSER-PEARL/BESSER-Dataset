





import java.util.List;
import java.util.ArrayList;

public class pivot_Namespace extends NamedElement {






    private pivot_Constraint pivot_constraint;




    private List<pivot_Constraint> pivot_constraints;


    public pivot_Namespace(
    ) {
        super(
        );
        this.pivot_constraints = new ArrayList<>();
    }

    public pivot_Namespace(
        ArrayList<pivot_Constraint> pivot_constraints    ) {
        this.pivot_constraints = pivot_constraints;
    }


    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }

}