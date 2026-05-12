





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_ConstraintDefinition  {

    private String checkOption;
    private boolean informationalConstraintSupported;
    private boolean clusteredUniqueConstraintSupported;
    private int maximumCheckExpressionLength;
    private int maximumPrimaryKeyIdentifierLength;
    private String parentDeleteDRIRuleType;
    private String parentUpdateDRIRuleType;
    private int maximumCheckConstraintIdentifierLength;
    private int maximumForeignKeyIdentifierLength;
    private boolean deferrableConstraintSupported;
    private boolean clusteredPrimaryKeySupported;
    private boolean uniqueKeyNullable;
    private boolean primaryKeyNullable;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_ConstraintDefinition(
        String checkOption,        boolean informationalConstraintSupported,        boolean clusteredUniqueConstraintSupported,        int maximumCheckExpressionLength,        int maximumPrimaryKeyIdentifierLength,        String parentDeleteDRIRuleType,        String parentUpdateDRIRuleType,        int maximumCheckConstraintIdentifierLength,        int maximumForeignKeyIdentifierLength,        boolean deferrableConstraintSupported,        boolean clusteredPrimaryKeySupported,        boolean uniqueKeyNullable,        boolean primaryKeyNullable    ) {
        this.checkOption = checkOption;
        this.informationalConstraintSupported = informationalConstraintSupported;
        this.clusteredUniqueConstraintSupported = clusteredUniqueConstraintSupported;
        this.maximumCheckExpressionLength = maximumCheckExpressionLength;
        this.maximumPrimaryKeyIdentifierLength = maximumPrimaryKeyIdentifierLength;
        this.parentDeleteDRIRuleType = parentDeleteDRIRuleType;
        this.parentUpdateDRIRuleType = parentUpdateDRIRuleType;
        this.maximumCheckConstraintIdentifierLength = maximumCheckConstraintIdentifierLength;
        this.maximumForeignKeyIdentifierLength = maximumForeignKeyIdentifierLength;
        this.deferrableConstraintSupported = deferrableConstraintSupported;
        this.clusteredPrimaryKeySupported = clusteredPrimaryKeySupported;
        this.uniqueKeyNullable = uniqueKeyNullable;
        this.primaryKeyNullable = primaryKeyNullable;
    }


    public String getCheckoption() {
        return checkOption;
    }

    public void setCheckoption(String checkOption) {
        this.checkOption = checkOption;
    }
    public boolean getInformationalconstraintsupported() {
        return informationalConstraintSupported;
    }

    public void setInformationalconstraintsupported(boolean informationalConstraintSupported) {
        this.informationalConstraintSupported = informationalConstraintSupported;
    }
    public boolean getClustereduniqueconstraintsupported() {
        return clusteredUniqueConstraintSupported;
    }

    public void setClustereduniqueconstraintsupported(boolean clusteredUniqueConstraintSupported) {
        this.clusteredUniqueConstraintSupported = clusteredUniqueConstraintSupported;
    }
    public int getMaximumcheckexpressionlength() {
        return maximumCheckExpressionLength;
    }

    public void setMaximumcheckexpressionlength(int maximumCheckExpressionLength) {
        this.maximumCheckExpressionLength = maximumCheckExpressionLength;
    }
    public int getMaximumprimarykeyidentifierlength() {
        return maximumPrimaryKeyIdentifierLength;
    }

    public void setMaximumprimarykeyidentifierlength(int maximumPrimaryKeyIdentifierLength) {
        this.maximumPrimaryKeyIdentifierLength = maximumPrimaryKeyIdentifierLength;
    }
    public String getParentdeletedriruletype() {
        return parentDeleteDRIRuleType;
    }

    public void setParentdeletedriruletype(String parentDeleteDRIRuleType) {
        this.parentDeleteDRIRuleType = parentDeleteDRIRuleType;
    }
    public String getParentupdatedriruletype() {
        return parentUpdateDRIRuleType;
    }

    public void setParentupdatedriruletype(String parentUpdateDRIRuleType) {
        this.parentUpdateDRIRuleType = parentUpdateDRIRuleType;
    }
    public int getMaximumcheckconstraintidentifierlength() {
        return maximumCheckConstraintIdentifierLength;
    }

    public void setMaximumcheckconstraintidentifierlength(int maximumCheckConstraintIdentifierLength) {
        this.maximumCheckConstraintIdentifierLength = maximumCheckConstraintIdentifierLength;
    }
    public int getMaximumforeignkeyidentifierlength() {
        return maximumForeignKeyIdentifierLength;
    }

    public void setMaximumforeignkeyidentifierlength(int maximumForeignKeyIdentifierLength) {
        this.maximumForeignKeyIdentifierLength = maximumForeignKeyIdentifierLength;
    }
    public boolean getDeferrableconstraintsupported() {
        return deferrableConstraintSupported;
    }

    public void setDeferrableconstraintsupported(boolean deferrableConstraintSupported) {
        this.deferrableConstraintSupported = deferrableConstraintSupported;
    }
    public boolean getClusteredprimarykeysupported() {
        return clusteredPrimaryKeySupported;
    }

    public void setClusteredprimarykeysupported(boolean clusteredPrimaryKeySupported) {
        this.clusteredPrimaryKeySupported = clusteredPrimaryKeySupported;
    }
    public boolean getUniquekeynullable() {
        return uniqueKeyNullable;
    }

    public void setUniquekeynullable(boolean uniqueKeyNullable) {
        this.uniqueKeyNullable = uniqueKeyNullable;
    }
    public boolean getPrimarykeynullable() {
        return primaryKeyNullable;
    }

    public void setPrimarykeynullable(boolean primaryKeyNullable) {
        this.primaryKeyNullable = primaryKeyNullable;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}