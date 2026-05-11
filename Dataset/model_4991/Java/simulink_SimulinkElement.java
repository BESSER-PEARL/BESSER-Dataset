





import java.util.List;
import java.util.ArrayList;

public class simulink_SimulinkElement  {

    private String name;





    private simulink_SimulinkReference simulink_simulinkreference;




    private simulink_IdentifierReference simulink_identifierreference;


    public simulink_SimulinkElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simulink_SimulinkReference getSimulink_simulinkreference() {
        return simulink_simulinkreference;
    }

    public void setSimulink_simulinkreference(simulink_SimulinkReference simulink_simulinkreference) {
        this.simulink_simulinkreference = simulink_simulinkreference;
    }
    public simulink_IdentifierReference getSimulink_identifierreference() {
        return simulink_identifierreference;
    }

    public void setSimulink_identifierreference(simulink_IdentifierReference simulink_identifierreference) {
        this.simulink_identifierreference = simulink_identifierreference;
    }

}