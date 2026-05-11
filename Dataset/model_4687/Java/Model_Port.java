





import java.util.List;
import java.util.ArrayList;

public class Model_Port  {

    private String portId;
    private String portType;





    private Model_DEVS model_devs;


    public Model_Port(
        String portId,        String portType    ) {
        this.portId = portId;
        this.portType = portType;
    }


    public String getPortid() {
        return portId;
    }

    public void setPortid(String portId) {
        this.portId = portId;
    }
    public String getPorttype() {
        return portType;
    }

    public void setPorttype(String portType) {
        this.portType = portType;
    }

    public Model_DEVS getModel_devs() {
        return model_devs;
    }

    public void setModel_devs(Model_DEVS model_devs) {
        this.model_devs = model_devs;
    }

}