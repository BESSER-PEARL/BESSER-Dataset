





import java.util.List;
import java.util.ArrayList;

public class internalsm_EventToken  {






    private internalsm_State internalsm_state;




    private List<internalsm_Event> internalsm_events;




    private internalsm_State internalsm_state;


    public internalsm_EventToken(
    ) {
        this.internalsm_events = new ArrayList<>();
    }

    public internalsm_EventToken(
        ArrayList<internalsm_Event> internalsm_events    ) {
        this.internalsm_events = internalsm_events;
    }


    public internalsm_State getInternalsm_state() {
        return internalsm_state;
    }

    public void setInternalsm_state(internalsm_State internalsm_state) {
        this.internalsm_state = internalsm_state;
    }
    public List<internalsm_Event> getInternalsm_events() {
        return internalsm_events;
    }

    public void addInternalsm_event(Internalsm_event internalsm_event) {
        this.internalsm_events.add(internalsm_event);
    }
    public internalsm_State getInternalsm_state() {
        return internalsm_state;
    }

    public void setInternalsm_state(internalsm_State internalsm_state) {
        this.internalsm_state = internalsm_state;
    }

}