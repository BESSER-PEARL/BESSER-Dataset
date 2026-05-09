





import java.util.List;
import java.util.ArrayList;

public class capellacommon_StateTransition extends ModelElement, NamedElement, CapellaElement {

    private String triggerDescription;
    private String kind;





    private capellacommon_Region capellacommon_region;




    private List<capellacommon_StateTransition> capellacommon_statetransitions;


    public capellacommon_StateTransition(
        String triggerDescription,        String kind    ) {
        super(
        );
        this.triggerDescription = triggerDescription;
        this.kind = kind;
        this.capellacommon_statetransitions = new ArrayList<>();
    }

    public capellacommon_StateTransition(
        String triggerDescription,        String kind        ArrayList<capellacommon_StateTransition> capellacommon_statetransitions    ) {
        this.triggerDescription = triggerDescription;
        this.kind = kind;
        this.capellacommon_statetransitions = capellacommon_statetransitions;
    }

    public String getTriggerdescription() {
        return triggerDescription;
    }

    public void setTriggerdescription(String triggerDescription) {
        this.triggerDescription = triggerDescription;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public capellacommon_Region getCapellacommon_region() {
        return capellacommon_region;
    }

    public void setCapellacommon_region(capellacommon_Region capellacommon_region) {
        this.capellacommon_region = capellacommon_region;
    }
    public List<capellacommon_StateTransition> getCapellacommon_statetransitions() {
        return capellacommon_statetransitions;
    }

    public void addCapellacommon_statetransition(Capellacommon_statetransition capellacommon_statetransition) {
        this.capellacommon_statetransitions.add(capellacommon_statetransition);
    }

}