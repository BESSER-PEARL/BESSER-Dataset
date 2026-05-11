





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Gateway extends FlowNode {

    private String gatewayDirection;



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


}