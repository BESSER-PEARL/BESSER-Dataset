





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_AreaRestriction extends restrictions_ConnectionRestrinctionA, restrictions_TaskGroupRestrictionA, restrictions_DeviceRestrictionA, restrictions_SignalGroupRestrictionA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, scenario_ModeDependentElementA, restrictions_SignalRestrictionA, restrictions_TaskRestrictionA, scenario_VariantDependentElementA {

    private boolean isForbidden;
    private String areaName;



    public oaam_restrictions_AreaRestriction(
        boolean isForbidden,        String areaName    ) {
        super(
        );
        this.isForbidden = isForbidden;
        this.areaName = areaName;
    }


    public boolean getIsforbidden() {
        return isForbidden;
    }

    public void setIsforbidden(boolean isForbidden) {
        this.isForbidden = isForbidden;
    }
    public String getAreaname() {
        return areaName;
    }

    public void setAreaname(String areaName) {
        this.areaName = areaName;
    }


}