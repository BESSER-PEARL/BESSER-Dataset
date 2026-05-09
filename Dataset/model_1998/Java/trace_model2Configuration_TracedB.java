





import java.util.List;
import java.util.ArrayList;

public class trace_model2Configuration_TracedB  {






    private List<B_b_State> b_b_states;


    public trace_model2Configuration_TracedB(
    ) {
        this.b_b_states = new ArrayList<>();
    }

    public trace_model2Configuration_TracedB(
        ArrayList<B_b_State> b_b_states    ) {
        this.b_b_states = b_b_states;
    }


    public List<B_b_State> getB_b_states() {
        return b_b_states;
    }

    public void addB_b_state(B_b_state b_b_state) {
        this.b_b_states.add(b_b_state);
    }

}