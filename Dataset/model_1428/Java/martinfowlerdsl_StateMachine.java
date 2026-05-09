





import java.util.List;
import java.util.ArrayList;

public class martinfowlerdsl_StateMachine  {






    private List<martinfowlerdsl_State> martinfowlerdsl_states;




    private martinfowlerdsl_State martinfowlerdsl_state;


    public martinfowlerdsl_StateMachine(
    ) {
        this.martinfowlerdsl_states = new ArrayList<>();
    }

    public martinfowlerdsl_StateMachine(
        ArrayList<martinfowlerdsl_State> martinfowlerdsl_states    ) {
        this.martinfowlerdsl_states = martinfowlerdsl_states;
    }


    public List<martinfowlerdsl_State> getMartinfowlerdsl_states() {
        return martinfowlerdsl_states;
    }

    public void addMartinfowlerdsl_state(Martinfowlerdsl_state martinfowlerdsl_state) {
        this.martinfowlerdsl_states.add(martinfowlerdsl_state);
    }
    public martinfowlerdsl_State getMartinfowlerdsl_state() {
        return martinfowlerdsl_state;
    }

    public void setMartinfowlerdsl_state(martinfowlerdsl_State martinfowlerdsl_state) {
        this.martinfowlerdsl_state = martinfowlerdsl_state;
    }

}