





import java.util.List;
import java.util.ArrayList;

public class rtsc_Port extends BehavioralElement {






    private rtsc_CoordinationProtocol rtsc_coordinationprotocol;




    private rtsc_Behavior rtsc_behavior;


    public rtsc_Port(
    ) {
        super(
        );
    }



    public rtsc_CoordinationProtocol getRtsc_coordinationprotocol() {
        return rtsc_coordinationprotocol;
    }

    public void setRtsc_coordinationprotocol(rtsc_CoordinationProtocol rtsc_coordinationprotocol) {
        this.rtsc_coordinationprotocol = rtsc_coordinationprotocol;
    }
    public rtsc_Behavior getRtsc_behavior() {
        return rtsc_behavior;
    }

    public void setRtsc_behavior(rtsc_Behavior rtsc_behavior) {
        this.rtsc_behavior = rtsc_behavior;
    }

}