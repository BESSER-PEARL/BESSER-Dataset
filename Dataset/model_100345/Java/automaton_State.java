





import java.util.List;
import java.util.ArrayList;

public class automaton_State  {

    private String label;





    private List<automaton_EventToken> automaton_eventtokens;




    private automaton_EventToken automaton_eventtoken;




    private automaton_Event automaton_event;


    public automaton_State(
        String label    ) {
        this.label = label;
        this.automaton_eventtokens = new ArrayList<>();
    }

    public automaton_State(
        String label        ArrayList<automaton_EventToken> automaton_eventtokens    ) {
        this.label = label;
        this.automaton_eventtokens = automaton_eventtokens;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<automaton_EventToken> getAutomaton_eventtokens() {
        return automaton_eventtokens;
    }

    public void addAutomaton_eventtoken(Automaton_eventtoken automaton_eventtoken) {
        this.automaton_eventtokens.add(automaton_eventtoken);
    }
    public automaton_EventToken getAutomaton_eventtoken() {
        return automaton_eventtoken;
    }

    public void setAutomaton_eventtoken(automaton_EventToken automaton_eventtoken) {
        this.automaton_eventtoken = automaton_eventtoken;
    }
    public automaton_Event getAutomaton_event() {
        return automaton_event;
    }

    public void setAutomaton_event(automaton_Event automaton_event) {
        this.automaton_event = automaton_event;
    }

}