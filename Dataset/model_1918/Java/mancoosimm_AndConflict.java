





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_AndConflict extends Conflict {






    private mancoosimm_Conflict mancoosimm_conflict;




    private mancoosimm_Conflict mancoosimm_conflict;




    private List<mancoosimm_Conflict> mancoosimm_conflicts;


    public mancoosimm_AndConflict(
    ) {
        super(
        );
        this.mancoosimm_conflicts = new ArrayList<>();
    }

    public mancoosimm_AndConflict(
        ArrayList<mancoosimm_Conflict> mancoosimm_conflicts    ) {
        this.mancoosimm_conflicts = mancoosimm_conflicts;
    }


    public mancoosimm_Conflict getMancoosimm_conflict() {
        return mancoosimm_conflict;
    }

    public void setMancoosimm_conflict(mancoosimm_Conflict mancoosimm_conflict) {
        this.mancoosimm_conflict = mancoosimm_conflict;
    }
    public mancoosimm_Conflict getMancoosimm_conflict() {
        return mancoosimm_conflict;
    }

    public void setMancoosimm_conflict(mancoosimm_Conflict mancoosimm_conflict) {
        this.mancoosimm_conflict = mancoosimm_conflict;
    }
    public List<mancoosimm_Conflict> getMancoosimm_conflicts() {
        return mancoosimm_conflicts;
    }

    public void addMancoosimm_conflict(Mancoosimm_conflict mancoosimm_conflict) {
        this.mancoosimm_conflicts.add(mancoosimm_conflict);
    }

}