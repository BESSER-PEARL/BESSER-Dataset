





import java.util.List;
import java.util.ArrayList;

public class automaton_EventToken  {






    private automaton_State automaton_state;




    private List<automaton_Event> automaton_events;




    private automaton_State automaton_state;




    private automaton_Event automaton_event;




    private automaton_Automaton automaton_automaton;


    public automaton_EventToken(
    ) {
        this.automaton_events = new ArrayList<>();
    }

    public automaton_EventToken(
        ArrayList<automaton_Event> automaton_events    ) {
        this.automaton_events = automaton_events;
    }


    public automaton_State getAutomaton_state() {
        return automaton_state;
    }

    public void setAutomaton_state(automaton_State automaton_state) {
        this.automaton_state = automaton_state;
    }
    public List<automaton_Event> getAutomaton_events() {
        return automaton_events;
    }

    public void addAutomaton_event(Automaton_event automaton_event) {
        this.automaton_events.add(automaton_event);
    }
    public automaton_State getAutomaton_state() {
        return automaton_state;
    }

    public void setAutomaton_state(automaton_State automaton_state) {
        this.automaton_state = automaton_state;
    }
    public automaton_Event getAutomaton_event() {
        return automaton_event;
    }

    public void setAutomaton_event(automaton_Event automaton_event) {
        this.automaton_event = automaton_event;
    }
    public automaton_Automaton getAutomaton_automaton() {
        return automaton_automaton;
    }

    public void setAutomaton_automaton(automaton_Automaton automaton_automaton) {
        this.automaton_automaton = automaton_automaton;
    }

}