





import java.util.List;
import java.util.ArrayList;

public class bpmn2_EventBasedGateway extends Gateway {

    private String eventGatewayType;
    private boolean instantiate;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_EventBasedGateway(
        String eventGatewayType,        boolean instantiate    ) {
        super(
        );
        this.eventGatewayType = eventGatewayType;
        this.instantiate = instantiate;
    }


    public String getEventgatewaytype() {
        return eventGatewayType;
    }

    public void setEventgatewaytype(String eventGatewayType) {
        this.eventGatewayType = eventGatewayType;
    }
    public boolean getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(boolean instantiate) {
        this.instantiate = instantiate;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}