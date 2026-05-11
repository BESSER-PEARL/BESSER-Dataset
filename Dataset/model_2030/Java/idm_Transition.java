





import java.util.List;
import java.util.ArrayList;

public class idm_Transition  {

    private String name;





    private idm_State idm_state;




    private idm_StateMachine idm_statemachine;




    private List<idm_State> idm_states;




    private idm_State idm_state;




    private List<idm_State> idm_states;


    public idm_Transition(
        String name    ) {
        this.name = name;
        this.idm_states = new ArrayList<>();
        this.idm_states = new ArrayList<>();
    }

    public idm_Transition(
        String name        ArrayList<idm_State> idm_states,        ArrayList<idm_State> idm_states    ) {
        this.name = name;
        this.idm_states = idm_states;
        this.idm_states = idm_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public idm_State getIdm_state() {
        return idm_state;
    }

    public void setIdm_state(idm_State idm_state) {
        this.idm_state = idm_state;
    }
    public idm_StateMachine getIdm_statemachine() {
        return idm_statemachine;
    }

    public void setIdm_statemachine(idm_StateMachine idm_statemachine) {
        this.idm_statemachine = idm_statemachine;
    }
    public List<idm_State> getIdm_states() {
        return idm_states;
    }

    public void addIdm_state(Idm_state idm_state) {
        this.idm_states.add(idm_state);
    }
    public idm_State getIdm_state() {
        return idm_state;
    }

    public void setIdm_state(idm_State idm_state) {
        this.idm_state = idm_state;
    }
    public List<idm_State> getIdm_states() {
        return idm_states;
    }

    public void addIdm_state(Idm_state idm_state) {
        this.idm_states.add(idm_state);
    }

}