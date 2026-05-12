





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_ViewDefinition  {

    private boolean checkOptionLevelsSupported;
    private boolean indexSupported;
    private int maximumIdentifierLength;
    private boolean checkOptionSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_ViewDefinition(
        boolean checkOptionLevelsSupported,        boolean indexSupported,        int maximumIdentifierLength,        boolean checkOptionSupported    ) {
        this.checkOptionLevelsSupported = checkOptionLevelsSupported;
        this.indexSupported = indexSupported;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.checkOptionSupported = checkOptionSupported;
    }


    public boolean getCheckoptionlevelssupported() {
        return checkOptionLevelsSupported;
    }

    public void setCheckoptionlevelssupported(boolean checkOptionLevelsSupported) {
        this.checkOptionLevelsSupported = checkOptionLevelsSupported;
    }
    public boolean getIndexsupported() {
        return indexSupported;
    }

    public void setIndexsupported(boolean indexSupported) {
        this.indexSupported = indexSupported;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public boolean getCheckoptionsupported() {
        return checkOptionSupported;
    }

    public void setCheckoptionsupported(boolean checkOptionSupported) {
        this.checkOptionSupported = checkOptionSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}