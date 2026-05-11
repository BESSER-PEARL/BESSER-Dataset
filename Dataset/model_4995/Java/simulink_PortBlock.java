





import java.util.List;
import java.util.ArrayList;

public class simulink_PortBlock extends Block {

    private int portNumber;





    private simulink_Port simulink_port;




    private simulink_Port simulink_port;


    public simulink_PortBlock(
        int portNumber    ) {
        super(
        );
        this.portNumber = portNumber;
    }


    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }

    public simulink_Port getSimulink_port() {
        return simulink_port;
    }

    public void setSimulink_port(simulink_Port simulink_port) {
        this.simulink_port = simulink_port;
    }
    public simulink_Port getSimulink_port() {
        return simulink_port;
    }

    public void setSimulink_port(simulink_Port simulink_port) {
        this.simulink_port = simulink_port;
    }

}