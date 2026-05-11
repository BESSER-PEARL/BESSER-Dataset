





import java.util.List;
import java.util.ArrayList;

public class simulink_IdentifierReference extends SimulinkReference {






    private simulink_ModelReference simulink_modelreference;


    public simulink_IdentifierReference(
    ) {
        super(
        );
    }



    public simulink_ModelReference getSimulink_modelreference() {
        return simulink_modelreference;
    }

    public void setSimulink_modelreference(simulink_ModelReference simulink_modelreference) {
        this.simulink_modelreference = simulink_modelreference;
    }

}