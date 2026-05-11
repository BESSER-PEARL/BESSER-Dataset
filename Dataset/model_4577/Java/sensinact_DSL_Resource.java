





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_Resource extends DSL_REF {

    private String gatewayID;
    private String resourceID;
    private String deviceID;
    private String serviceID;





    private sensinact_DSL_SENSINACT sensinact_dsl_sensinact;


    public sensinact_DSL_Resource(
        String gatewayID,        String resourceID,        String deviceID,        String serviceID    ) {
        super(
        );
        this.gatewayID = gatewayID;
        this.resourceID = resourceID;
        this.deviceID = deviceID;
        this.serviceID = serviceID;
    }


    public String getGatewayid() {
        return gatewayID;
    }

    public void setGatewayid(String gatewayID) {
        this.gatewayID = gatewayID;
    }
    public String getResourceid() {
        return resourceID;
    }

    public void setResourceid(String resourceID) {
        this.resourceID = resourceID;
    }
    public String getDeviceid() {
        return deviceID;
    }

    public void setDeviceid(String deviceID) {
        this.deviceID = deviceID;
    }
    public String getServiceid() {
        return serviceID;
    }

    public void setServiceid(String serviceID) {
        this.serviceID = serviceID;
    }

    public sensinact_DSL_SENSINACT getSensinact_dsl_sensinact() {
        return sensinact_dsl_sensinact;
    }

    public void setSensinact_dsl_sensinact(sensinact_DSL_SENSINACT sensinact_dsl_sensinact) {
        this.sensinact_dsl_sensinact = sensinact_dsl_sensinact;
    }

}