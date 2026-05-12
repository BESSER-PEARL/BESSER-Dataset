





import java.util.List;
import java.util.ArrayList;

public class petrinetv3Trace_States_Place_tokens_Value  {






    private List<State> states;




    private petrinetv3_TracedPlace petrinetv3_tracedplace;




    private List<petrinetv3_TracedToken> petrinetv3_tracedtokens;


    public petrinetv3Trace_States_Place_tokens_Value(
    ) {
        this.states = new ArrayList<>();
        this.petrinetv3_tracedtokens = new ArrayList<>();
    }

    public petrinetv3Trace_States_Place_tokens_Value(
        ArrayList<State> states,        ArrayList<petrinetv3_TracedToken> petrinetv3_tracedtokens    ) {
        this.states = states;
        this.petrinetv3_tracedtokens = petrinetv3_tracedtokens;
    }


    public List<State> getStates() {
        return states;
    }

    public void addState(State state) {
        this.states.add(state);
    }
    public petrinetv3_TracedPlace getPetrinetv3_tracedplace() {
        return petrinetv3_tracedplace;
    }

    public void setPetrinetv3_tracedplace(petrinetv3_TracedPlace petrinetv3_tracedplace) {
        this.petrinetv3_tracedplace = petrinetv3_tracedplace;
    }
    public List<petrinetv3_TracedToken> getPetrinetv3_tracedtokens() {
        return petrinetv3_tracedtokens;
    }

    public void addPetrinetv3_tracedtoken(Petrinetv3_tracedtoken petrinetv3_tracedtoken) {
        this.petrinetv3_tracedtokens.add(petrinetv3_tracedtoken);
    }

}