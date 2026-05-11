





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_Device  {

    private String name;





    private wsmodel3_IoTNode wsmodel3_iotnode;


    public wsmodel3_Device(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public wsmodel3_IoTNode getWsmodel3_iotnode() {
        return wsmodel3_iotnode;
    }

    public void setWsmodel3_iotnode(wsmodel3_IoTNode wsmodel3_iotnode) {
        this.wsmodel3_iotnode = wsmodel3_iotnode;
    }

}