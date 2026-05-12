





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_DebuggerDefinition  {

    private boolean conditionSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_DebuggerDefinition(
        boolean conditionSupported    ) {
        this.conditionSupported = conditionSupported;
    }


    public boolean getConditionsupported() {
        return conditionSupported;
    }

    public void setConditionsupported(boolean conditionSupported) {
        this.conditionSupported = conditionSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}