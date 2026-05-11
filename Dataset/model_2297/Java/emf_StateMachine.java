





import java.util.List;
import java.util.ArrayList;

public class emf_StateMachine  {






    private emf_State emf_state;




    private List<emf_State> emf_states;


    public emf_StateMachine(
    ) {
        this.emf_states = new ArrayList<>();
    }

    public emf_StateMachine(
        ArrayList<emf_State> emf_states    ) {
        this.emf_states = emf_states;
    }


    public emf_State getEmf_state() {
        return emf_state;
    }

    public void setEmf_state(emf_State emf_state) {
        this.emf_state = emf_state;
    }
    public List<emf_State> getEmf_states() {
        return emf_states;
    }

    public void addEmf_state(Emf_state emf_state) {
        this.emf_states.add(emf_state);
    }

}