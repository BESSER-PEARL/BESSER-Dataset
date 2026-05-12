





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_ColumnDefinition  {

    private int maximumIdentifierLength;
    private boolean computedSupported;
    private boolean identityMinimumSupported;
    private boolean identityStartValueSupported;
    private boolean identityMaximumSupported;
    private boolean identitySupported;
    private boolean identityCycleSupported;
    private boolean identityIncrementSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;




    private List<dbdefinition_PredefinedDataTypeDefinition> dbdefinition_predefineddatatypedefinitions;


    public dbdefinition_ColumnDefinition(
        int maximumIdentifierLength,        boolean computedSupported,        boolean identityMinimumSupported,        boolean identityStartValueSupported,        boolean identityMaximumSupported,        boolean identitySupported,        boolean identityCycleSupported,        boolean identityIncrementSupported    ) {
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.computedSupported = computedSupported;
        this.identityMinimumSupported = identityMinimumSupported;
        this.identityStartValueSupported = identityStartValueSupported;
        this.identityMaximumSupported = identityMaximumSupported;
        this.identitySupported = identitySupported;
        this.identityCycleSupported = identityCycleSupported;
        this.identityIncrementSupported = identityIncrementSupported;
        this.dbdefinition_predefineddatatypedefinitions = new ArrayList<>();
    }

    public dbdefinition_ColumnDefinition(
        int maximumIdentifierLength,        boolean computedSupported,        boolean identityMinimumSupported,        boolean identityStartValueSupported,        boolean identityMaximumSupported,        boolean identitySupported,        boolean identityCycleSupported,        boolean identityIncrementSupported        ArrayList<dbdefinition_PredefinedDataTypeDefinition> dbdefinition_predefineddatatypedefinitions    ) {
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.computedSupported = computedSupported;
        this.identityMinimumSupported = identityMinimumSupported;
        this.identityStartValueSupported = identityStartValueSupported;
        this.identityMaximumSupported = identityMaximumSupported;
        this.identitySupported = identitySupported;
        this.identityCycleSupported = identityCycleSupported;
        this.identityIncrementSupported = identityIncrementSupported;
        this.dbdefinition_predefineddatatypedefinitions = dbdefinition_predefineddatatypedefinitions;
    }

    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public boolean getComputedsupported() {
        return computedSupported;
    }

    public void setComputedsupported(boolean computedSupported) {
        this.computedSupported = computedSupported;
    }
    public boolean getIdentityminimumsupported() {
        return identityMinimumSupported;
    }

    public void setIdentityminimumsupported(boolean identityMinimumSupported) {
        this.identityMinimumSupported = identityMinimumSupported;
    }
    public boolean getIdentitystartvaluesupported() {
        return identityStartValueSupported;
    }

    public void setIdentitystartvaluesupported(boolean identityStartValueSupported) {
        this.identityStartValueSupported = identityStartValueSupported;
    }
    public boolean getIdentitymaximumsupported() {
        return identityMaximumSupported;
    }

    public void setIdentitymaximumsupported(boolean identityMaximumSupported) {
        this.identityMaximumSupported = identityMaximumSupported;
    }
    public boolean getIdentitysupported() {
        return identitySupported;
    }

    public void setIdentitysupported(boolean identitySupported) {
        this.identitySupported = identitySupported;
    }
    public boolean getIdentitycyclesupported() {
        return identityCycleSupported;
    }

    public void setIdentitycyclesupported(boolean identityCycleSupported) {
        this.identityCycleSupported = identityCycleSupported;
    }
    public boolean getIdentityincrementsupported() {
        return identityIncrementSupported;
    }

    public void setIdentityincrementsupported(boolean identityIncrementSupported) {
        this.identityIncrementSupported = identityIncrementSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }
    public List<dbdefinition_PredefinedDataTypeDefinition> getDbdefinition_predefineddatatypedefinitions() {
        return dbdefinition_predefineddatatypedefinitions;
    }

    public void addDbdefinition_predefineddatatypedefinition(Dbdefinition_predefineddatatypedefinition dbdefinition_predefineddatatypedefinition) {
        this.dbdefinition_predefineddatatypedefinitions.add(dbdefinition_predefineddatatypedefinition);
    }

}