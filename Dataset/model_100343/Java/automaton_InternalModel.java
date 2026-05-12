





import java.util.List;
import java.util.ArrayList;

public class automaton_InternalModel  {






    private List<automaton_EventToken> automaton_eventtokens;




    private automaton_Event automaton_event;


    public automaton_InternalModel(
    ) {
        this.automaton_eventtokens = new ArrayList<>();
    }

    public automaton_InternalModel(
        ArrayList<automaton_EventToken> automaton_eventtokens    ) {
        this.automaton_eventtokens = automaton_eventtokens;
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

}