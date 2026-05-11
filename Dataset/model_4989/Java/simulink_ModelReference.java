





import java.util.List;
import java.util.ArrayList;

public class simulink_ModelReference extends Block {






    private simulink_IdentifierReference simulink_identifierreference;




    private simulink_SimulinkModel simulink_simulinkmodel;


    public simulink_ModelReference(
    ) {
        super(
        );
    }



    public simulink_IdentifierReference getSimulink_identifierreference() {
        return simulink_identifierreference;
    }

    public void setSimulink_identifierreference(simulink_IdentifierReference simulink_identifierreference) {
        this.simulink_identifierreference = simulink_identifierreference;
    }
    public simulink_SimulinkModel getSimulink_simulinkmodel() {
        return simulink_simulinkmodel;
    }

    public void setSimulink_simulinkmodel(simulink_SimulinkModel simulink_simulinkmodel) {
        this.simulink_simulinkmodel = simulink_simulinkmodel;
    }

}