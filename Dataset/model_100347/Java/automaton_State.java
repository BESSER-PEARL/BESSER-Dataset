





import java.util.List;
import java.util.ArrayList;

public class automaton_State  {

    private String label;





    private List<automaton_TimedZone> automaton_timedzones;




    private automaton_TimedZone automaton_timedzone;




    private automaton_TimedZone automaton_timedzone;




    private List<automaton_EventToken> automaton_eventtokens;




    private automaton_Event automaton_event;




    private List<automaton_TimedZone> automaton_timedzones;




    private automaton_Automaton automaton_automaton;




    private automaton_EventToken automaton_eventtoken;


    public automaton_State(
        String label    ) {
        this.label = label;
        this.automaton_timedzones = new ArrayList<>();
        this.automaton_eventtokens = new ArrayList<>();
        this.automaton_timedzones = new ArrayList<>();
    }

    public automaton_State(
        String label        ArrayList<automaton_TimedZone> automaton_timedzones,        ArrayList<automaton_EventToken> automaton_eventtokens,        ArrayList<automaton_TimedZone> automaton_timedzones    ) {
        this.label = label;
        this.automaton_timedzones = automaton_timedzones;
        this.automaton_eventtokens = automaton_eventtokens;
        this.automaton_timedzones = automaton_timedzones;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<automaton_TimedZone> getAutomaton_timedzones() {
        return automaton_timedzones;
    }

    public void addAutomaton_timedzone(Automaton_timedzone automaton_timedzone) {
        this.automaton_timedzones.add(automaton_timedzone);
    }
    public automaton_TimedZone getAutomaton_timedzone() {
        return automaton_timedzone;
    }

    public void setAutomaton_timedzone(automaton_TimedZone automaton_timedzone) {
        this.automaton_timedzone = automaton_timedzone;
    }
    public automaton_TimedZone getAutomaton_timedzone() {
        return automaton_timedzone;
    }

    public void setAutomaton_timedzone(automaton_TimedZone automaton_timedzone) {
        this.automaton_timedzone = automaton_timedzone;
    }
    public List<automaton_EventToken> getAutomaton_eventtokens() {
        return automaton_eventtokens;
    }

    public void addAutomaton_eventtoken(Automaton_eventtoken automaton_eventtoken) {
        this.automaton_eventtokens.add(automaton_eventtoken);
    }
    public automaton_Event getAutomaton_event() {
        return automaton_event;
    }

    public void setAutomaton_event(automaton_Event automaton_event) {
        this.automaton_event = automaton_event;
    }
    public List<automaton_TimedZone> getAutomaton_timedzones() {
        return automaton_timedzones;
    }

    public void addAutomaton_timedzone(Automaton_timedzone automaton_timedzone) {
        this.automaton_timedzones.add(automaton_timedzone);
    }
    public automaton_Automaton getAutomaton_automaton() {
        return automaton_automaton;
    }

    public void setAutomaton_automaton(automaton_Automaton automaton_automaton) {
        this.automaton_automaton = automaton_automaton;
    }
    public automaton_EventToken getAutomaton_eventtoken() {
        return automaton_eventtoken;
    }

    public void setAutomaton_eventtoken(automaton_EventToken automaton_eventtoken) {
        this.automaton_eventtoken = automaton_eventtoken;
    }

}