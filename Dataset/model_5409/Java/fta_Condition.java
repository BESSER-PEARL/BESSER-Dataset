





import java.util.List;
import java.util.ArrayList;

public class fta_Condition extends Diagram {

    private String GateKind;





    private fta_Event fta_event;




    private List<fta_Event> fta_events;




    private fta_Hazard fta_hazard;


    public fta_Condition(
        String GateKind    ) {
        super(
        );
        this.GateKind = GateKind;
        this.fta_events = new ArrayList<>();
    }

    public fta_Condition(
        String GateKind        ArrayList<fta_Event> fta_events    ) {
        this.GateKind = GateKind;
        this.fta_events = fta_events;
    }

    public String getGatekind() {
        return GateKind;
    }

    public void setGatekind(String GateKind) {
        this.GateKind = GateKind;
    }

    public fta_Event getFta_event() {
        return fta_event;
    }

    public void setFta_event(fta_Event fta_event) {
        this.fta_event = fta_event;
    }
    public List<fta_Event> getFta_events() {
        return fta_events;
    }

    public void addFta_event(Fta_event fta_event) {
        this.fta_events.add(fta_event);
    }
    public fta_Hazard getFta_hazard() {
        return fta_hazard;
    }

    public void setFta_hazard(fta_Hazard fta_hazard) {
        this.fta_hazard = fta_hazard;
    }

}