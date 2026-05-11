





import java.util.List;
import java.util.ArrayList;

public class SecCon_StateMachineScenario extends NamedElement {

    private String author;
    private String version;





    private List<SecCon_Event> seccon_events;




    private List<SecCon_Transition> seccon_transitions;


    public SecCon_StateMachineScenario(
        String author,        String version    ) {
        super(
        );
        this.author = author;
        this.version = version;
        this.seccon_events = new ArrayList<>();
        this.seccon_transitions = new ArrayList<>();
    }

    public SecCon_StateMachineScenario(
        String author,        String version        ArrayList<SecCon_Event> seccon_events,        ArrayList<SecCon_Transition> seccon_transitions    ) {
        this.author = author;
        this.version = version;
        this.seccon_events = seccon_events;
        this.seccon_transitions = seccon_transitions;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<SecCon_Event> getSeccon_events() {
        return seccon_events;
    }

    public void addSeccon_event(Seccon_event seccon_event) {
        this.seccon_events.add(seccon_event);
    }
    public List<SecCon_Transition> getSeccon_transitions() {
        return seccon_transitions;
    }

    public void addSeccon_transition(Seccon_transition seccon_transition) {
        this.seccon_transitions.add(seccon_transition);
    }

}