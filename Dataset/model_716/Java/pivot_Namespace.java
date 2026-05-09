





import java.util.List;
import java.util.ArrayList;

public class pivot_Namespace extends NamedElement {






    private List<pivot_Constraint> pivot_constraints;




    private pivot_Constraint pivot_constraint;




    private pivot_Import pivot_import;


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


    public List<pivot_Constraint> getPivot_constraints() {
        return pivot_constraints;
    }

    public void addPivot_constraint(Pivot_constraint pivot_constraint) {
        this.pivot_constraints.add(pivot_constraint);
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_Import getPivot_import() {
        return pivot_import;
    }

    public void setPivot_import(pivot_Import pivot_import) {
        this.pivot_import = pivot_import;
    }

}