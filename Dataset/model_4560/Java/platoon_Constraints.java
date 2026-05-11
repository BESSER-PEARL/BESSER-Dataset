





import java.util.List;
import java.util.ArrayList;

public class platoon_Constraints  {






    private List<platoon_Constraint> platoon_constraints;




    private platoon_World platoon_world;


    public platoon_Constraints(
    ) {
        this.platoon_constraints = new ArrayList<>();
    }

    public platoon_Constraints(
        ArrayList<platoon_Constraint> platoon_constraints    ) {
        this.platoon_constraints = platoon_constraints;
    }


    public List<platoon_Constraint> getPlatoon_constraints() {
        return platoon_constraints;
    }

    public void addPlatoon_constraint(Platoon_constraint platoon_constraint) {
        this.platoon_constraints.add(platoon_constraint);
    }
    public platoon_World getPlatoon_world() {
        return platoon_world;
    }

    public void setPlatoon_world(platoon_World platoon_world) {
        this.platoon_world = platoon_world;
    }

}