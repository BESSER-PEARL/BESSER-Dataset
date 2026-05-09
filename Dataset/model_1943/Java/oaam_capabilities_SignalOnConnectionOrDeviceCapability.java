





import java.util.List;
import java.util.ArrayList;

public class oaam_capabilities_SignalOnConnectionOrDeviceCapability extends common_OaamBaseElementA, capabilities_CapabilityA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float worstCaseTransmissionTime;



    public oaam_capabilities_SignalOnConnectionOrDeviceCapability(
        float worstCaseTransmissionTime    ) {
        super(
        );
        this.worstCaseTransmissionTime = worstCaseTransmissionTime;
    }


    public float getWorstcasetransmissiontime() {
        return worstCaseTransmissionTime;
    }

    public void setWorstcasetransmissiontime(float worstCaseTransmissionTime) {
        this.worstCaseTransmissionTime = worstCaseTransmissionTime;
    }


}