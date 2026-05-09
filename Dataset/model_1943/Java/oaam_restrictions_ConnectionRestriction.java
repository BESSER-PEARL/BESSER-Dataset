





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_ConnectionRestriction extends restrictions_SignalGroupRestrictionA, common_OaamBaseElementA, scenario_ModeDependentElementA, restrictions_SubfunctionRestrictionA, restrictions_SignalRestrictionA, scenario_VariantDependentElementA {

    private boolean isForbidden;
    private String connectionName;



    public oaam_restrictions_ConnectionRestriction(
        boolean isForbidden,        String connectionName    ) {
        super(
        );
        this.isForbidden = isForbidden;
        this.connectionName = connectionName;
    }


    public boolean getIsforbidden() {
        return isForbidden;
    }

    public void setIsforbidden(boolean isForbidden) {
        this.isForbidden = isForbidden;
    }
    public String getConnectionname() {
        return connectionName;
    }

    public void setConnectionname(String connectionName) {
        this.connectionName = connectionName;
    }


}