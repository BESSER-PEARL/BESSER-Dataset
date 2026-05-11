





import java.util.List;
import java.util.ArrayList;

public class Model_Port  {

    private String portId;





    private Model_Event model_event;




    private Model_DEVS model_devs;


    public Model_Port(
        String portId    ) {
        this.portId = portId;
    }


    public String getPortid() {
        return portId;
    }

    public void setPortid(String portId) {
        this.portId = portId;
    }

    public Model_Event getModel_event() {
        return model_event;
    }

    public void setModel_event(Model_Event model_event) {
        this.model_event = model_event;
    }
    public Model_DEVS getModel_devs() {
        return model_devs;
    }

    public void setModel_devs(Model_DEVS model_devs) {
        this.model_devs = model_devs;
    }

}