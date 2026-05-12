





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_UserDefinedTypeDefinition  {

    private int maximumIdentifierLength;
    private boolean structuredTypeSupported;
    private boolean defaultValueSupported;
    private boolean distinctTypeSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_UserDefinedTypeDefinition(
        int maximumIdentifierLength,        boolean structuredTypeSupported,        boolean defaultValueSupported,        boolean distinctTypeSupported    ) {
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.structuredTypeSupported = structuredTypeSupported;
        this.defaultValueSupported = defaultValueSupported;
        this.distinctTypeSupported = distinctTypeSupported;
    }


    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public boolean getStructuredtypesupported() {
        return structuredTypeSupported;
    }

    public void setStructuredtypesupported(boolean structuredTypeSupported) {
        this.structuredTypeSupported = structuredTypeSupported;
    }
    public boolean getDefaultvaluesupported() {
        return defaultValueSupported;
    }

    public void setDefaultvaluesupported(boolean defaultValueSupported) {
        this.defaultValueSupported = defaultValueSupported;
    }
    public boolean getDistincttypesupported() {
        return distinctTypeSupported;
    }

    public void setDistincttypesupported(boolean distinctTypeSupported) {
        this.distinctTypeSupported = distinctTypeSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}