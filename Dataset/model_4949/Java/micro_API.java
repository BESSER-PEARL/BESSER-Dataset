





import java.util.List;
import java.util.ArrayList;

public class micro_API extends NamedElement {






    private List<micro_Event> micro_events;




    private micro_Event micro_event;


    public micro_API(
    ) {
        super(
        );
        this.micro_events = new ArrayList<>();
    }

    public micro_API(
        ArrayList<micro_Event> micro_events    ) {
        this.micro_events = micro_events;
    }


    public List<micro_Event> getMicro_events() {
        return micro_events;
    }

    public void addMicro_event(Micro_event micro_event) {
        this.micro_events.add(micro_event);
    }
    public micro_Event getMicro_event() {
        return micro_event;
    }

    public void setMicro_event(micro_Event micro_event) {
        this.micro_event = micro_event;
    }

}