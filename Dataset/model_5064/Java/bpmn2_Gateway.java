





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Gateway extends FlowNode {

    private String gatewayDirection;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Gateway(
        String gatewayDirection    ) {
        super(
        );
        this.gatewayDirection = gatewayDirection;
    }


    public String getGatewaydirection() {
        return gatewayDirection;
    }

    public void setGatewaydirection(String gatewayDirection) {
        this.gatewayDirection = gatewayDirection;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}