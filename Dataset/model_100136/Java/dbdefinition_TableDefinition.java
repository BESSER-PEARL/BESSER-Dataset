





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_TableDefinition  {

    private boolean validProcSupported;
    private boolean dataCaptureSupported;
    private boolean editProcSupported;
    private boolean encodingSupported;
    private int maximumIdentifierLength;
    private boolean auditSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_TableDefinition(
        boolean validProcSupported,        boolean dataCaptureSupported,        boolean editProcSupported,        boolean encodingSupported,        int maximumIdentifierLength,        boolean auditSupported    ) {
        this.validProcSupported = validProcSupported;
        this.dataCaptureSupported = dataCaptureSupported;
        this.editProcSupported = editProcSupported;
        this.encodingSupported = encodingSupported;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.auditSupported = auditSupported;
    }


    public boolean getValidprocsupported() {
        return validProcSupported;
    }

    public void setValidprocsupported(boolean validProcSupported) {
        this.validProcSupported = validProcSupported;
    }
    public boolean getDatacapturesupported() {
        return dataCaptureSupported;
    }

    public void setDatacapturesupported(boolean dataCaptureSupported) {
        this.dataCaptureSupported = dataCaptureSupported;
    }
    public boolean getEditprocsupported() {
        return editProcSupported;
    }

    public void setEditprocsupported(boolean editProcSupported) {
        this.editProcSupported = editProcSupported;
    }
    public boolean getEncodingsupported() {
        return encodingSupported;
    }

    public void setEncodingsupported(boolean encodingSupported) {
        this.encodingSupported = encodingSupported;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public boolean getAuditsupported() {
        return auditSupported;
    }

    public void setAuditsupported(boolean auditSupported) {
        this.auditSupported = auditSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}