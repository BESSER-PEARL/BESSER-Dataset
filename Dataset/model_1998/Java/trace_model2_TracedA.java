





import java.util.List;
import java.util.ArrayList;

public class trace_model2_TracedA  {






    private List<A_a_State> a_a_states;


    public trace_model2_TracedA(
    ) {
        this.a_a_states = new ArrayList<>();
    }

    public trace_model2_TracedA(
        ArrayList<A_a_State> a_a_states    ) {
        this.a_a_states = a_a_states;
    }


    public List<A_a_State> getA_a_states() {
        return a_a_states;
    }

    public void addA_a_state(A_a_state a_a_state) {
        this.a_a_states.add(a_a_state);
    }

}