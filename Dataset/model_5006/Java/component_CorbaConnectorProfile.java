





import java.util.List;
import java.util.ArrayList;

public class component_CorbaConnectorProfile extends ConnectorProfile {

    private String rtcConnectorProfile;



    public component_CorbaConnectorProfile(
        String rtcConnectorProfile    ) {
        super(
        );
        this.rtcConnectorProfile = rtcConnectorProfile;
    }


    public String getRtcconnectorprofile() {
        return rtcConnectorProfile;
    }

    public void setRtcconnectorprofile(String rtcConnectorProfile) {
        this.rtcConnectorProfile = rtcConnectorProfile;
    }


}