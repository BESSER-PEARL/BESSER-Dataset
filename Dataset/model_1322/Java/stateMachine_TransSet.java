





import java.util.List;
import java.util.ArrayList;

public class stateMachine_TransSet  {






    private List<stateMachine_Trans> statemachine_transs;




    private stateMachine_State statemachine_state;




    private stateMachine_Role statemachine_role;


    public stateMachine_TransSet(
    ) {
        this.statemachine_transs = new ArrayList<>();
    }

    public stateMachine_TransSet(
        ArrayList<stateMachine_Trans> statemachine_transs    ) {
        this.statemachine_transs = statemachine_transs;
    }


    public List<stateMachine_Trans> getStatemachine_transs() {
        return statemachine_transs;
    }

    public void addStatemachine_trans(Statemachine_trans statemachine_trans) {
        this.statemachine_transs.add(statemachine_trans);
    }
    public stateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(stateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public stateMachine_Role getStatemachine_role() {
        return statemachine_role;
    }

    public void setStatemachine_role(stateMachine_Role statemachine_role) {
        this.statemachine_role = statemachine_role;
    }

}