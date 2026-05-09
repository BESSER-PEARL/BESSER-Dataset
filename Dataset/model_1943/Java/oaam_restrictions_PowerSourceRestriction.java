





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_PowerSourceRestriction extends restrictions_TaskGroupRestrictionA, restrictions_SignalGroupRestrictionA, common_OaamBaseElementA, scenario_ModeDependentElementA, restrictions_SubfunctionRestrictionA, scenario_VariantDependentElementA, restrictions_SignalRestrictionA, restrictions_TaskRestrictionA, restrictions_DeviceRestrictionA {

    private String powerSourceName;
    private boolean isForbidden;



    public oaam_restrictions_PowerSourceRestriction(
        String powerSourceName,        boolean isForbidden    ) {
        super(
        );
        this.powerSourceName = powerSourceName;
        this.isForbidden = isForbidden;
    }


    public String getPowersourcename() {
        return powerSourceName;
    }

    public void setPowersourcename(String powerSourceName) {
        this.powerSourceName = powerSourceName;
    }
    public boolean getIsforbidden() {
        return isForbidden;
    }

    public void setIsforbidden(boolean isForbidden) {
        this.isForbidden = isForbidden;
    }


}