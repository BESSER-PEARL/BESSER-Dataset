





import java.util.List;
import java.util.ArrayList;

public class automaton_EventToken  {






    private automaton_InternalModel automaton_internalmodel;




    private automaton_Event automaton_event;




    private List<automaton_Event> automaton_events;




    private automaton_Automaton automaton_automaton;




    private List<automaton_TimedZone> automaton_timedzones;


    public automaton_EventToken(
    ) {
        this.automaton_events = new ArrayList<>();
        this.automaton_timedzones = new ArrayList<>();
    }

    public automaton_EventToken(
        ArrayList<automaton_Event> automaton_events,        ArrayList<automaton_TimedZone> automaton_timedzones    ) {
        this.automaton_events = automaton_events;
        this.automaton_timedzones = automaton_timedzones;
    }


    public automaton_InternalModel getAutomaton_internalmodel() {
        return automaton_internalmodel;
    }

    public void setAutomaton_internalmodel(automaton_InternalModel automaton_internalmodel) {
        this.automaton_internalmodel = automaton_internalmodel;
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
    public automaton_Automaton getAutomaton_automaton() {
        return automaton_automaton;
    }

    public void setAutomaton_automaton(automaton_Automaton automaton_automaton) {
        this.automaton_automaton = automaton_automaton;
    }
    public List<automaton_TimedZone> getAutomaton_timedzones() {
        return automaton_timedzones;
    }

    public void addAutomaton_timedzone(Automaton_timedzone automaton_timedzone) {
        this.automaton_timedzones.add(automaton_timedzone);
    }

}