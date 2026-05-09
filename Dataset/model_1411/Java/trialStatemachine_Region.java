





import java.util.List;
import java.util.ArrayList;

public class trialStatemachine_Region  {

    private String history;





    private trialStatemachine_State trialstatemachine_state;




    private List<trialStatemachine_State> trialstatemachine_states;




    private trialStatemachine_ComplexState trialstatemachine_complexstate;




    private trialStatemachine_State trialstatemachine_state;


    public trialStatemachine_Region(
        String history    ) {
        this.history = history;
        this.trialstatemachine_states = new ArrayList<>();
    }

    public trialStatemachine_Region(
        String history        ArrayList<trialStatemachine_State> trialstatemachine_states    ) {
        this.history = history;
        this.trialstatemachine_states = trialstatemachine_states;
    }

    public String getHistory() {
        return history;
    }

    public void setHistory(String history) {
        this.history = history;
    }

    public trialStatemachine_State getTrialstatemachine_state() {
        return trialstatemachine_state;
    }

    public void setTrialstatemachine_state(trialStatemachine_State trialstatemachine_state) {
        this.trialstatemachine_state = trialstatemachine_state;
    }
    public List<trialStatemachine_State> getTrialstatemachine_states() {
        return trialstatemachine_states;
    }

    public void addTrialstatemachine_state(Trialstatemachine_state trialstatemachine_state) {
        this.trialstatemachine_states.add(trialstatemachine_state);
    }
    public trialStatemachine_ComplexState getTrialstatemachine_complexstate() {
        return trialstatemachine_complexstate;
    }

    public void setTrialstatemachine_complexstate(trialStatemachine_ComplexState trialstatemachine_complexstate) {
        this.trialstatemachine_complexstate = trialstatemachine_complexstate;
    }
    public trialStatemachine_State getTrialstatemachine_state() {
        return trialstatemachine_state;
    }

    public void setTrialstatemachine_state(trialStatemachine_State trialstatemachine_state) {
        this.trialstatemachine_state = trialstatemachine_state;
    }

}