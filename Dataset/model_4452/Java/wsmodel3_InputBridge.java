





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_InputBridge extends Bridge {

    private String URI;





    private wsmodel3_Actuator wsmodel3_actuator;


    public wsmodel3_InputBridge(
        String URI    ) {
        super(
        );
        this.URI = URI;
    }


    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public wsmodel3_Actuator getWsmodel3_actuator() {
        return wsmodel3_actuator;
    }

    public void setWsmodel3_actuator(wsmodel3_Actuator wsmodel3_actuator) {
        this.wsmodel3_actuator = wsmodel3_actuator;
    }

}