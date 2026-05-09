





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_LocationRestriction extends restrictions_ConnectionRestrinctionA, restrictions_TaskGroupRestrictionA, restrictions_DeviceRestrictionA, restrictions_SignalGroupRestrictionA, common_OaamBaseElementA, scenario_ModeDependentElementA, restrictions_SubfunctionRestrictionA, restrictions_SignalRestrictionA, restrictions_TaskRestrictionA, scenario_VariantDependentElementA {

    private boolean isForbidden;
    private String locationName;



    public oaam_restrictions_LocationRestriction(
        boolean isForbidden,        String locationName    ) {
        super(
        );
        this.isForbidden = isForbidden;
        this.locationName = locationName;
    }


    public boolean getIsforbidden() {
        return isForbidden;
    }

    public void setIsforbidden(boolean isForbidden) {
        this.isForbidden = isForbidden;
    }
    public String getLocationname() {
        return locationName;
    }

    public void setLocationname(String locationName) {
        this.locationName = locationName;
    }


}