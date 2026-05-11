





import java.util.List;
import java.util.ArrayList;

public class component_CorbaPortSynchronizer extends PortSynchronizer, CorbaWrapperObject {

    private String rTCPortProfile;



    public component_CorbaPortSynchronizer(
        String rTCPortProfile    ) {
        super(
        );
        this.rTCPortProfile = rTCPortProfile;
    }


    public String getRtcportprofile() {
        return rTCPortProfile;
    }

    public void setRtcportprofile(String rTCPortProfile) {
        this.rTCPortProfile = rTCPortProfile;
    }


}