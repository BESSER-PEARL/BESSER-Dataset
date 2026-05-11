





import java.util.List;
import java.util.ArrayList;

public class sipme_Capability extends EnterpriseObject {

    private String capabilityType;



    public sipme_Capability(
        String capabilityType    ) {
        super(
        );
        this.capabilityType = capabilityType;
    }


    public String getCapabilitytype() {
        return capabilityType;
    }

    public void setCapabilitytype(String capabilityType) {
        this.capabilityType = capabilityType;
    }


}