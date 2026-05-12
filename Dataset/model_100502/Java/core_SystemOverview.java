





import java.util.List;
import java.util.ArrayList;

public class core_SystemOverview extends ContractualElement {

    private String capabilities;
    private String purpose;





    private List<core_Goal> core_goals;




    private core_EObject core_eobject;




    private List<core_SystemContext> core_systemcontexts;




    private List<core_Variable> core_variables;


    public core_SystemOverview(
        String capabilities,        String purpose    ) {
        super(
        );
        this.capabilities = capabilities;
        this.purpose = purpose;
        this.core_goals = new ArrayList<>();
        this.core_systemcontexts = new ArrayList<>();
        this.core_variables = new ArrayList<>();
    }

    public core_SystemOverview(
        String capabilities,        String purpose        ArrayList<core_Goal> core_goals,        ArrayList<core_SystemContext> core_systemcontexts,        ArrayList<core_Variable> core_variables    ) {
        this.capabilities = capabilities;
        this.purpose = purpose;
        this.core_goals = core_goals;
        this.core_systemcontexts = core_systemcontexts;
        this.core_variables = core_variables;
    }

    public String getCapabilities() {
        return capabilities;
    }

    public void setCapabilities(String capabilities) {
        this.capabilities = capabilities;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }

    public List<core_Goal> getCore_goals() {
        return core_goals;
    }

    public void addCore_goal(Core_goal core_goal) {
        this.core_goals.add(core_goal);
    }
    public core_EObject getCore_eobject() {
        return core_eobject;
    }

    public void setCore_eobject(core_EObject core_eobject) {
        this.core_eobject = core_eobject;
    }
    public List<core_SystemContext> getCore_systemcontexts() {
        return core_systemcontexts;
    }

    public void addCore_systemcontext(Core_systemcontext core_systemcontext) {
        this.core_systemcontexts.add(core_systemcontext);
    }
    public List<core_Variable> getCore_variables() {
        return core_variables;
    }

    public void addCore_variable(Core_variable core_variable) {
        this.core_variables.add(core_variable);
    }

}