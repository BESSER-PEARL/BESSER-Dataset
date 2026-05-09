





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_BottomPattern extends CorePattern {






    private List<EnforcementOperation> enforcementoperations;




    private List<RealizedVariable> realizedvariables;




    private Area area;




    private List<Assignment> assignments;


    public FlatQVT_BottomPattern(
    ) {
        super(
        );
        this.enforcementoperations = new ArrayList<>();
        this.realizedvariables = new ArrayList<>();
        this.assignments = new ArrayList<>();
    }

    public FlatQVT_BottomPattern(
        ArrayList<EnforcementOperation> enforcementoperations,        ArrayList<RealizedVariable> realizedvariables,        ArrayList<Assignment> assignments    ) {
        this.enforcementoperations = enforcementoperations;
        this.realizedvariables = realizedvariables;
        this.assignments = assignments;
    }


    public List<EnforcementOperation> getEnforcementoperations() {
        return enforcementoperations;
    }

    public void addEnforcementoperation(Enforcementoperation enforcementoperation) {
        this.enforcementoperations.add(enforcementoperation);
    }
    public List<RealizedVariable> getRealizedvariables() {
        return realizedvariables;
    }

    public void addRealizedvariable(Realizedvariable realizedvariable) {
        this.realizedvariables.add(realizedvariable);
    }
    public Area getArea() {
        return area;
    }

    public void setArea(Area area) {
        this.area = area;
    }
    public List<Assignment> getAssignments() {
        return assignments;
    }

    public void addAssignment(Assignment assignment) {
        this.assignments.add(assignment);
    }

}