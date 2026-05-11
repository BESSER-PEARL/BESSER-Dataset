





import java.util.List;
import java.util.ArrayList;

public class core_Specification extends VerifiableElement {

    private String version;





    private List<core_VerificationActivity> core_verificationactivitys;




    private List<core_EObject> core_eobjects;




    private List<core_Actor> core_actors;




    private List<core_Conflict> core_conflicts;




    private List<core_EObject> core_eobjects;




    private core_SystemOverview core_systemoverview;


    public core_Specification(
        String version    ) {
        super(
        );
        this.version = version;
        this.core_verificationactivitys = new ArrayList<>();
        this.core_eobjects = new ArrayList<>();
        this.core_actors = new ArrayList<>();
        this.core_conflicts = new ArrayList<>();
        this.core_eobjects = new ArrayList<>();
    }

    public core_Specification(
        String version        ArrayList<core_VerificationActivity> core_verificationactivitys,        ArrayList<core_EObject> core_eobjects,        ArrayList<core_Actor> core_actors,        ArrayList<core_Conflict> core_conflicts,        ArrayList<core_EObject> core_eobjects    ) {
        this.version = version;
        this.core_verificationactivitys = core_verificationactivitys;
        this.core_eobjects = core_eobjects;
        this.core_actors = core_actors;
        this.core_conflicts = core_conflicts;
        this.core_eobjects = core_eobjects;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<core_VerificationActivity> getCore_verificationactivitys() {
        return core_verificationactivitys;
    }

    public void addCore_verificationactivity(Core_verificationactivity core_verificationactivity) {
        this.core_verificationactivitys.add(core_verificationactivity);
    }
    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }
    public List<core_Actor> getCore_actors() {
        return core_actors;
    }

    public void addCore_actor(Core_actor core_actor) {
        this.core_actors.add(core_actor);
    }
    public List<core_Conflict> getCore_conflicts() {
        return core_conflicts;
    }

    public void addCore_conflict(Core_conflict core_conflict) {
        this.core_conflicts.add(core_conflict);
    }
    public List<core_EObject> getCore_eobjects() {
        return core_eobjects;
    }

    public void addCore_eobject(Core_eobject core_eobject) {
        this.core_eobjects.add(core_eobject);
    }
    public core_SystemOverview getCore_systemoverview() {
        return core_systemoverview;
    }

    public void setCore_systemoverview(core_SystemOverview core_systemoverview) {
        this.core_systemoverview = core_systemoverview;
    }

}