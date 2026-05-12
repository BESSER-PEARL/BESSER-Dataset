





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_TriggerDefinition  {

    private boolean whenClauseSupported;
    private boolean insteadOfTriggerSupported;
    private boolean tableTriggerReferenceSupported;
    private boolean rowTriggerReferenceSupported;
    private int maximumIdentifierLength;
    private int maximumActionBodyLength;
    private boolean referencesClauseSupported;
    private int maximumReferencePartLength;
    private boolean perColumnUpdateTriggerSupported;
    private boolean typeSupported;
    private boolean granularitySupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_TriggerDefinition(
        boolean whenClauseSupported,        boolean insteadOfTriggerSupported,        boolean tableTriggerReferenceSupported,        boolean rowTriggerReferenceSupported,        int maximumIdentifierLength,        int maximumActionBodyLength,        boolean referencesClauseSupported,        int maximumReferencePartLength,        boolean perColumnUpdateTriggerSupported,        boolean typeSupported,        boolean granularitySupported    ) {
        this.whenClauseSupported = whenClauseSupported;
        this.insteadOfTriggerSupported = insteadOfTriggerSupported;
        this.tableTriggerReferenceSupported = tableTriggerReferenceSupported;
        this.rowTriggerReferenceSupported = rowTriggerReferenceSupported;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.maximumActionBodyLength = maximumActionBodyLength;
        this.referencesClauseSupported = referencesClauseSupported;
        this.maximumReferencePartLength = maximumReferencePartLength;
        this.perColumnUpdateTriggerSupported = perColumnUpdateTriggerSupported;
        this.typeSupported = typeSupported;
        this.granularitySupported = granularitySupported;
    }


    public boolean getWhenclausesupported() {
        return whenClauseSupported;
    }

    public void setWhenclausesupported(boolean whenClauseSupported) {
        this.whenClauseSupported = whenClauseSupported;
    }
    public boolean getInsteadoftriggersupported() {
        return insteadOfTriggerSupported;
    }

    public void setInsteadoftriggersupported(boolean insteadOfTriggerSupported) {
        this.insteadOfTriggerSupported = insteadOfTriggerSupported;
    }
    public boolean getTabletriggerreferencesupported() {
        return tableTriggerReferenceSupported;
    }

    public void setTabletriggerreferencesupported(boolean tableTriggerReferenceSupported) {
        this.tableTriggerReferenceSupported = tableTriggerReferenceSupported;
    }
    public boolean getRowtriggerreferencesupported() {
        return rowTriggerReferenceSupported;
    }

    public void setRowtriggerreferencesupported(boolean rowTriggerReferenceSupported) {
        this.rowTriggerReferenceSupported = rowTriggerReferenceSupported;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public int getMaximumactionbodylength() {
        return maximumActionBodyLength;
    }

    public void setMaximumactionbodylength(int maximumActionBodyLength) {
        this.maximumActionBodyLength = maximumActionBodyLength;
    }
    public boolean getReferencesclausesupported() {
        return referencesClauseSupported;
    }

    public void setReferencesclausesupported(boolean referencesClauseSupported) {
        this.referencesClauseSupported = referencesClauseSupported;
    }
    public int getMaximumreferencepartlength() {
        return maximumReferencePartLength;
    }

    public void setMaximumreferencepartlength(int maximumReferencePartLength) {
        this.maximumReferencePartLength = maximumReferencePartLength;
    }
    public boolean getPercolumnupdatetriggersupported() {
        return perColumnUpdateTriggerSupported;
    }

    public void setPercolumnupdatetriggersupported(boolean perColumnUpdateTriggerSupported) {
        this.perColumnUpdateTriggerSupported = perColumnUpdateTriggerSupported;
    }
    public boolean getTypesupported() {
        return typeSupported;
    }

    public void setTypesupported(boolean typeSupported) {
        this.typeSupported = typeSupported;
    }
    public boolean getGranularitysupported() {
        return granularitySupported;
    }

    public void setGranularitysupported(boolean granularitySupported) {
        this.granularitySupported = granularitySupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}