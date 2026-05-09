





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_DeviceTypeRestriction extends restrictions_TaskGroupRestrictionA, restrictions_SignalGroupRestrictionA, common_OaamBaseElementA, scenario_ModeDependentElementA, restrictions_SubfunctionRestrictionA, restrictions_SignalRestrictionA, restrictions_TaskRestrictionA, scenario_VariantDependentElementA {

    private boolean isForbidden;
    private String deviceTypeName;



    public oaam_restrictions_DeviceTypeRestriction(
        boolean isForbidden,        String deviceTypeName    ) {
        super(
        );
        this.isForbidden = isForbidden;
        this.deviceTypeName = deviceTypeName;
    }


    public boolean getIsforbidden() {
        return isForbidden;
    }

    public void setIsforbidden(boolean isForbidden) {
        this.isForbidden = isForbidden;
    }
    public String getDevicetypename() {
        return deviceTypeName;
    }

    public void setDevicetypename(String deviceTypeName) {
        this.deviceTypeName = deviceTypeName;
    }


}