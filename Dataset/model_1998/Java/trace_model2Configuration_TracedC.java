





import java.util.List;
import java.util.ArrayList;

public class trace_model2Configuration_TracedC  {






    private List<C_c_State> c_c_states;


    public trace_model2Configuration_TracedC(
    ) {
        this.c_c_states = new ArrayList<>();
    }

    public trace_model2Configuration_TracedC(
        ArrayList<C_c_State> c_c_states    ) {
        this.c_c_states = c_c_states;
    }


    public List<C_c_State> getC_c_states() {
        return c_c_states;
    }

    public void addC_c_state(C_c_state c_c_state) {
        this.c_c_states.add(c_c_state);
    }

}