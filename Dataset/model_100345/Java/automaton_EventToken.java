





import java.util.List;
import java.util.ArrayList;

public class automaton_EventToken  {






    private automaton_Event automaton_event;




    private List<automaton_Event> automaton_events;


    public automaton_EventToken(
    ) {
        this.automaton_events = new ArrayList<>();
    }

    public automaton_EventToken(
        ArrayList<automaton_Event> automaton_events    ) {
        this.automaton_events = automaton_events;
    }


    public automaton_Event getAutomaton_event() {
        return automaton_event;
    }

    public void setAutomaton_event(automaton_Event automaton_event) {
        this.automaton_event = automaton_event;
    }
    public List<automaton_Event> getAutomaton_events() {
        return automaton_events;
    }

    public void addAutomaton_event(Automaton_event automaton_event) {
        this.automaton_events.add(automaton_event);
    }

}