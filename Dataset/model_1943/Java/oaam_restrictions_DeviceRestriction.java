





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_DeviceRestriction extends restrictions_TaskGroupRestrictionA, restrictions_SignalGroupRestrictionA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, scenario_ModeDependentElementA, restrictions_SignalRestrictionA, restrictions_TaskRestrictionA, scenario_VariantDependentElementA {

    private String deviceName;
    private boolean isForbidden;



    public oaam_restrictions_DeviceRestriction(
        String deviceName,        boolean isForbidden    ) {
        super(
        );
        this.deviceName = deviceName;
        this.isForbidden = isForbidden;
    }


    public String getDevicename() {
        return deviceName;
    }

    public void setDevicename(String deviceName) {
        this.deviceName = deviceName;
    }
    public boolean getIsforbidden() {
        return isForbidden;
    }

    public void setIsforbidden(boolean isForbidden) {
        this.isForbidden = isForbidden;
    }


}