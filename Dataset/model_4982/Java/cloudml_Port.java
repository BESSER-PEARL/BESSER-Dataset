





import java.util.List;
import java.util.ArrayList;

public class cloudml_Port extends CloudMLElementWithProperties {

    private int portNumber;
    private boolean isLocal;





    private cloudml_Component cloudml_component;


    public cloudml_Port(
        int portNumber,        boolean isLocal    ) {
        super(
        );
        this.portNumber = portNumber;
        this.isLocal = isLocal;
    }


    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }
    public boolean getIslocal() {
        return isLocal;
    }

    public void setIslocal(boolean isLocal) {
        this.isLocal = isLocal;
    }

    public cloudml_Component getCloudml_component() {
        return cloudml_component;
    }

    public void setCloudml_component(cloudml_Component cloudml_component) {
        this.cloudml_component = cloudml_component;
    }

}