





import java.util.List;
import java.util.ArrayList;

public class SecCon_State extends StateVertex {






    private List<SecCon_Event> seccon_events;




    private List<SecCon_StateOperation> seccon_stateoperations;


    public SecCon_State(
    ) {
        super(
        );
        this.seccon_events = new ArrayList<>();
        this.seccon_stateoperations = new ArrayList<>();
    }

    public SecCon_State(
        ArrayList<SecCon_Event> seccon_events,        ArrayList<SecCon_StateOperation> seccon_stateoperations    ) {
        this.seccon_events = seccon_events;
        this.seccon_stateoperations = seccon_stateoperations;
    }


    public List<SecCon_Event> getSeccon_events() {
        return seccon_events;
    }

    public void addSeccon_event(Seccon_event seccon_event) {
        this.seccon_events.add(seccon_event);
    }
    public List<SecCon_StateOperation> getSeccon_stateoperations() {
        return seccon_stateoperations;
    }

    public void addSeccon_stateoperation(Seccon_stateoperation seccon_stateoperation) {
        this.seccon_stateoperations.add(seccon_stateoperation);
    }

}