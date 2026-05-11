





import java.util.List;
import java.util.ArrayList;

public class core_Goal extends ContractualElement {

    private String priority;





    private core_Conflict core_conflict;




    private List<core_Conflict> core_conflicts;


    public core_Goal(
        String priority    ) {
        super(
        );
        this.priority = priority;
        this.core_conflicts = new ArrayList<>();
    }

    public core_Goal(
        String priority        ArrayList<core_Conflict> core_conflicts    ) {
        this.priority = priority;
        this.core_conflicts = core_conflicts;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public core_Conflict getCore_conflict() {
        return core_conflict;
    }

    public void setCore_conflict(core_Conflict core_conflict) {
        this.core_conflict = core_conflict;
    }
    public List<core_Conflict> getCore_conflicts() {
        return core_conflicts;
    }

    public void addCore_conflict(Core_conflict core_conflict) {
        this.core_conflicts.add(core_conflict);
    }

}