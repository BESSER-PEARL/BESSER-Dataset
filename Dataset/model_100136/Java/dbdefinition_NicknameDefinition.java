





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_NicknameDefinition  {

    private boolean indexSupported;
    private boolean constraintSupported;
    private int maximumIdentifierLength;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_NicknameDefinition(
        boolean indexSupported,        boolean constraintSupported,        int maximumIdentifierLength    ) {
        this.indexSupported = indexSupported;
        this.constraintSupported = constraintSupported;
        this.maximumIdentifierLength = maximumIdentifierLength;
    }


    public boolean getIndexsupported() {
        return indexSupported;
    }

    public void setIndexsupported(boolean indexSupported) {
        this.indexSupported = indexSupported;
    }
    public boolean getConstraintsupported() {
        return constraintSupported;
    }

    public void setConstraintsupported(boolean constraintSupported) {
        this.constraintSupported = constraintSupported;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}