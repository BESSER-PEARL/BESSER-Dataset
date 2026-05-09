





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_ConnectionTypeRestriction extends restrictions_SignalGroupRestrictionA, common_OaamBaseElementA, restrictions_SubfunctionRestrictionA, scenario_ModeDependentElementA, restrictions_SignalRestrictionA, scenario_VariantDependentElementA {

    private String connectionTypeName;
    private boolean isForbidden;



    public oaam_restrictions_ConnectionTypeRestriction(
        String connectionTypeName,        boolean isForbidden    ) {
        super(
        );
        this.connectionTypeName = connectionTypeName;
        this.isForbidden = isForbidden;
    }


    public String getConnectiontypename() {
        return connectionTypeName;
    }

    public void setConnectiontypename(String connectionTypeName) {
        this.connectionTypeName = connectionTypeName;
    }
    public boolean getIsforbidden() {
        return isForbidden;
    }

    public void setIsforbidden(boolean isForbidden) {
        this.isForbidden = isForbidden;
    }


}