





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Gateway extends FlowNode {

    private String gatewayDirection;



    public BPMN2Model_Gateway(
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