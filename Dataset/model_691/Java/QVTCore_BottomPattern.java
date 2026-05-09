





import java.util.List;
import java.util.ArrayList;

public class QVTCore_BottomPattern extends CorePattern {






    private List<Assignment> assignments;




    private List<EnforcementOperation> enforcementoperations;




    private Area area;




    private List<RealizedVariable> realizedvariables;


    public QVTCore_BottomPattern(
    ) {
        super(
        );
        this.assignments = new ArrayList<>();
        this.enforcementoperations = new ArrayList<>();
        this.realizedvariables = new ArrayList<>();
    }

    public QVTCore_BottomPattern(
        ArrayList<Assignment> assignments,        ArrayList<EnforcementOperation> enforcementoperations,        ArrayList<RealizedVariable> realizedvariables    ) {
        this.assignments = assignments;
        this.enforcementoperations = enforcementoperations;
        this.realizedvariables = realizedvariables;
    }


    public List<Assignment> getAssignments() {
        return assignments;
    }

    public void addAssignment(Assignment assignment) {
        this.assignments.add(assignment);
    }
    public List<EnforcementOperation> getEnforcementoperations() {
        return enforcementoperations;
    }

    public void addEnforcementoperation(Enforcementoperation enforcementoperation) {
        this.enforcementoperations.add(enforcementoperation);
    }
    public Area getArea() {
        return area;
    }

    public void setArea(Area area) {
        this.area = area;
    }
    public List<RealizedVariable> getRealizedvariables() {
        return realizedvariables;
    }

    public void addRealizedvariable(Realizedvariable realizedvariable) {
        this.realizedvariables.add(realizedvariable);
    }

}