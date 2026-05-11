





import java.util.List;
import java.util.ArrayList;

public class simulink_MultiConnection extends Connection {






    private simulink_SingleConnection simulink_singleconnection;




    private List<simulink_SingleConnection> simulink_singleconnections;


    public simulink_MultiConnection(
    ) {
        super(
        );
        this.simulink_singleconnections = new ArrayList<>();
    }

    public simulink_MultiConnection(
        ArrayList<simulink_SingleConnection> simulink_singleconnections    ) {
        this.simulink_singleconnections = simulink_singleconnections;
    }


    public simulink_SingleConnection getSimulink_singleconnection() {
        return simulink_singleconnection;
    }

    public void setSimulink_singleconnection(simulink_SingleConnection simulink_singleconnection) {
        this.simulink_singleconnection = simulink_singleconnection;
    }
    public List<simulink_SingleConnection> getSimulink_singleconnections() {
        return simulink_singleconnections;
    }

    public void addSimulink_singleconnection(Simulink_singleconnection simulink_singleconnection) {
        this.simulink_singleconnections.add(simulink_singleconnection);
    }

}