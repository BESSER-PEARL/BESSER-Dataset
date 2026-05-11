





import java.util.List;
import java.util.ArrayList;

public class bpmn2_EventBasedGateway extends Gateway {

    private boolean instantiate;
    private String eventGatewayType;



    public bpmn2_EventBasedGateway(
        boolean instantiate,        String eventGatewayType    ) {
        super(
        );
        this.instantiate = instantiate;
        this.eventGatewayType = eventGatewayType;
    }


    public boolean getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(boolean instantiate) {
        this.instantiate = instantiate;
    }
    public String getEventgatewaytype() {
        return eventGatewayType;
    }

    public void setEventgatewaytype(String eventGatewayType) {
        this.eventGatewayType = eventGatewayType;
    }


}