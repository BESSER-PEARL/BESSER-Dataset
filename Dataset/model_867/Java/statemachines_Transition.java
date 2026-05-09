





import java.util.List;
import java.util.ArrayList;

public class statemachines_Transition extends NamedElement {

    private String kind;





    private statemachines_Region statemachines_region;




    private statemachines_Region statemachines_region;




    private List<statemachines_Trigger> statemachines_triggers;


    public statemachines_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.statemachines_triggers = new ArrayList<>();
    }

    public statemachines_Transition(
        String kind        ArrayList<statemachines_Trigger> statemachines_triggers    ) {
        this.kind = kind;
        this.statemachines_triggers = statemachines_triggers;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public statemachines_Region getStatemachines_region() {
        return statemachines_region;
    }

    public void setStatemachines_region(statemachines_Region statemachines_region) {
        this.statemachines_region = statemachines_region;
    }
    public statemachines_Region getStatemachines_region() {
        return statemachines_region;
    }

    public void setStatemachines_region(statemachines_Region statemachines_region) {
        this.statemachines_region = statemachines_region;
    }
    public List<statemachines_Trigger> getStatemachines_triggers() {
        return statemachines_triggers;
    }

    public void addStatemachines_trigger(Statemachines_trigger statemachines_trigger) {
        this.statemachines_triggers.add(statemachines_trigger);
    }

}