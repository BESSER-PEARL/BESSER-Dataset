





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_Resource extends DSL_REF {

    private String deviceID;
    private String gatewayID;
    private String serviceID;
    private String resourceID;



    public sensinact_DSL_Resource(
        String deviceID,        String gatewayID,        String serviceID,        String resourceID    ) {
        super(
        );
        this.deviceID = deviceID;
        this.gatewayID = gatewayID;
        this.serviceID = serviceID;
        this.resourceID = resourceID;
    }


    public String getDeviceid() {
        return deviceID;
    }

    public void setDeviceid(String deviceID) {
        this.deviceID = deviceID;
    }
    public String getGatewayid() {
        return gatewayID;
    }

    public void setGatewayid(String gatewayID) {
        this.gatewayID = gatewayID;
    }
    public String getServiceid() {
        return serviceID;
    }

    public void setServiceid(String serviceID) {
        this.serviceID = serviceID;
    }
    public String getResourceid() {
        return resourceID;
    }

    public void setResourceid(String resourceID) {
        this.resourceID = resourceID;
    }


}