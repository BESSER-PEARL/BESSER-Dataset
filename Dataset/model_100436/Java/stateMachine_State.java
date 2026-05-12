





import java.util.List;
import java.util.ArrayList;

public class stateMachine_State  {

    private String nombre;





    private stateMachine_State statemachine_state;




    private stateMachine_StateMachine statemachine_statemachine;




    private List<stateMachine_State> statemachine_states;


    public stateMachine_State(
        String nombre    ) {
        this.nombre = nombre;
        this.statemachine_states = new ArrayList<>();
    }

    public stateMachine_State(
        String nombre        ArrayList<stateMachine_State> statemachine_states    ) {
        this.nombre = nombre;
        this.statemachine_states = statemachine_states;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public stateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(stateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public stateMachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(stateMachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public List<stateMachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }

}