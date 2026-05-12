





import java.util.List;
import java.util.ArrayList;

public class stateMachine_StateMachine  {

    private String nombre;





    private stateMachine_Properties statemachine_properties;


    public stateMachine_StateMachine(
        String nombre    ) {
        this.nombre = nombre;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public stateMachine_Properties getStatemachine_properties() {
        return statemachine_properties;
    }

    public void setStatemachine_properties(stateMachine_Properties statemachine_properties) {
        this.statemachine_properties = statemachine_properties;
    }

}