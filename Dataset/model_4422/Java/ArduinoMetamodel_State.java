





import java.util.List;
import java.util.ArrayList;

public class ArduinoMetamodel_State  {

    private String name;
    private boolean isInitial;





    private ArduinoMetamodel_FiniteStateMachine arduinometamodel_finitestatemachine;


    public ArduinoMetamodel_State(
        String name,        boolean isInitial    ) {
        this.name = name;
        this.isInitial = isInitial;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }

    public ArduinoMetamodel_FiniteStateMachine getArduinometamodel_finitestatemachine() {
        return arduinometamodel_finitestatemachine;
    }

    public void setArduinometamodel_finitestatemachine(ArduinoMetamodel_FiniteStateMachine arduinometamodel_finitestatemachine) {
        this.arduinometamodel_finitestatemachine = arduinometamodel_finitestatemachine;
    }

}