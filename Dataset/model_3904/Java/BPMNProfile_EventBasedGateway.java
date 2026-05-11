





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_EventBasedGateway extends Gateway {

    private String instantiate;
    private String eventGatewayType;



    public BPMNProfile_EventBasedGateway(
        String instantiate,        String eventGatewayType    ) {
        super(
        );
        this.instantiate = instantiate;
        this.eventGatewayType = eventGatewayType;
    }


    public String getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(String instantiate) {
        this.instantiate = instantiate;
    }
    public String getEventgatewaytype() {
        return eventGatewayType;
    }

    public void setEventgatewaytype(String eventGatewayType) {
        this.eventGatewayType = eventGatewayType;
    }


}