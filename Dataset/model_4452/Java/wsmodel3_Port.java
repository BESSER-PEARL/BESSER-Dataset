





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_Port  {

    private String type;
    private String id;





    private wsmodel3_Controller wsmodel3_controller;


    public wsmodel3_Port(
        String type,        String id    ) {
        this.type = type;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public wsmodel3_Controller getWsmodel3_controller() {
        return wsmodel3_controller;
    }

    public void setWsmodel3_controller(wsmodel3_Controller wsmodel3_controller) {
        this.wsmodel3_controller = wsmodel3_controller;
    }

}