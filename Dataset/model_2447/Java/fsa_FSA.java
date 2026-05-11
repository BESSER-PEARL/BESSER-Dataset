





import java.util.List;
import java.util.ArrayList;

public class fsa_FSA  {

    private String temporalFormula;





    private fsa_State fsa_state;




    private List<fsa_State> fsa_states;




    private fsa_State fsa_state;


    public fsa_FSA(
        String temporalFormula    ) {
        this.temporalFormula = temporalFormula;
        this.fsa_states = new ArrayList<>();
    }

    public fsa_FSA(
        String temporalFormula        ArrayList<fsa_State> fsa_states    ) {
        this.temporalFormula = temporalFormula;
        this.fsa_states = fsa_states;
    }

    public String getTemporalformula() {
        return temporalFormula;
    }

    public void setTemporalformula(String temporalFormula) {
        this.temporalFormula = temporalFormula;
    }

    public fsa_State getFsa_state() {
        return fsa_state;
    }

    public void setFsa_state(fsa_State fsa_state) {
        this.fsa_state = fsa_state;
    }
    public List<fsa_State> getFsa_states() {
        return fsa_states;
    }

    public void addFsa_state(Fsa_state fsa_state) {
        this.fsa_states.add(fsa_state);
    }
    public fsa_State getFsa_state() {
        return fsa_state;
    }

    public void setFsa_state(fsa_State fsa_state) {
        this.fsa_state = fsa_state;
    }

}