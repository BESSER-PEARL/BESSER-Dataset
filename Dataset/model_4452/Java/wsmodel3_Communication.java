





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_Communication  {

    private String name;
    private String type;





    private wsmodel3_MessageBroker wsmodel3_messagebroker;




    private wsmodel3_AccesPoint wsmodel3_accespoint;




    private wsmodel3_Controller wsmodel3_controller;


    public wsmodel3_Communication(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public wsmodel3_MessageBroker getWsmodel3_messagebroker() {
        return wsmodel3_messagebroker;
    }

    public void setWsmodel3_messagebroker(wsmodel3_MessageBroker wsmodel3_messagebroker) {
        this.wsmodel3_messagebroker = wsmodel3_messagebroker;
    }
    public wsmodel3_AccesPoint getWsmodel3_accespoint() {
        return wsmodel3_accespoint;
    }

    public void setWsmodel3_accespoint(wsmodel3_AccesPoint wsmodel3_accespoint) {
        this.wsmodel3_accespoint = wsmodel3_accespoint;
    }
    public wsmodel3_Controller getWsmodel3_controller() {
        return wsmodel3_controller;
    }

    public void setWsmodel3_controller(wsmodel3_Controller wsmodel3_controller) {
        this.wsmodel3_controller = wsmodel3_controller;
    }

}