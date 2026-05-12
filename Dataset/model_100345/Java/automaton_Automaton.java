





import java.util.List;
import java.util.ArrayList;

public class automaton_Automaton  {

    private String eventPatternId;





    private List<automaton_EventToken> automaton_eventtokens;




    private List<automaton_State> automaton_states;




    private automaton_InternalModel automaton_internalmodel;




    private automaton_InternalModel automaton_internalmodel;


    public automaton_Automaton(
        String eventPatternId    ) {
        this.eventPatternId = eventPatternId;
        this.automaton_eventtokens = new ArrayList<>();
        this.automaton_states = new ArrayList<>();
    }

    public automaton_Automaton(
        String eventPatternId        ArrayList<automaton_EventToken> automaton_eventtokens,        ArrayList<automaton_State> automaton_states    ) {
        this.eventPatternId = eventPatternId;
        this.automaton_eventtokens = automaton_eventtokens;
        this.automaton_states = automaton_states;
    }

    public String getEventpatternid() {
        return eventPatternId;
    }

    public void setEventpatternid(String eventPatternId) {
        this.eventPatternId = eventPatternId;
    }

    public List<automaton_EventToken> getAutomaton_eventtokens() {
        return automaton_eventtokens;
    }

    public void addAutomaton_eventtoken(Automaton_eventtoken automaton_eventtoken) {
        this.automaton_eventtokens.add(automaton_eventtoken);
    }
    public List<automaton_State> getAutomaton_states() {
        return automaton_states;
    }

    public void addAutomaton_state(Automaton_state automaton_state) {
        this.automaton_states.add(automaton_state);
    }
    public automaton_InternalModel getAutomaton_internalmodel() {
        return automaton_internalmodel;
    }

    public void setAutomaton_internalmodel(automaton_InternalModel automaton_internalmodel) {
        this.automaton_internalmodel = automaton_internalmodel;
    }
    public automaton_InternalModel getAutomaton_internalmodel() {
        return automaton_internalmodel;
    }

    public void setAutomaton_internalmodel(automaton_InternalModel automaton_internalmodel) {
        this.automaton_internalmodel = automaton_internalmodel;
    }

}