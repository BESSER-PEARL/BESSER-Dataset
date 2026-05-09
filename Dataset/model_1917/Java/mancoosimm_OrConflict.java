





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_OrConflict extends Conflict {






    private mancoosimm_Conflict mancoosimm_conflict;




    private List<mancoosimm_Conflict> mancoosimm_conflicts;




    private mancoosimm_Conflict mancoosimm_conflict;


    public mancoosimm_OrConflict(
    ) {
        super(
        );
        this.mancoosimm_conflicts = new ArrayList<>();
    }

    public mancoosimm_OrConflict(
        ArrayList<mancoosimm_Conflict> mancoosimm_conflicts    ) {
        this.mancoosimm_conflicts = mancoosimm_conflicts;
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
    public mancoosimm_Conflict getMancoosimm_conflict() {
        return mancoosimm_conflict;
    }

    public void setMancoosimm_conflict(mancoosimm_Conflict mancoosimm_conflict) {
        this.mancoosimm_conflict = mancoosimm_conflict;
    }

}