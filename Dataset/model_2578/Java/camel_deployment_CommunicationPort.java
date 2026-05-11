





import java.util.List;
import java.util.ArrayList;

public class camel_deployment_CommunicationPort extends DeploymentElement {

    private int portNumber;



    public camel_deployment_CommunicationPort(
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


}