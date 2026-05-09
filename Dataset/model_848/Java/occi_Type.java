





import java.util.List;
import java.util.ArrayList;

public class occi_Type extends Category {






    private List<occi_Constraint> occi_constraints;


    public occi_Type(
    ) {
        super(
        );
        this.occi_constraints = new ArrayList<>();
    }

    public occi_Type(
        ArrayList<occi_Constraint> occi_constraints    ) {
        this.occi_constraints = occi_constraints;
    }


    public List<occi_Constraint> getOcci_constraints() {
        return occi_constraints;
    }

    public void addOcci_constraint(Occi_constraint occi_constraint) {
        this.occi_constraints.add(occi_constraint);
    }

}