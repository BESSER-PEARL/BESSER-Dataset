





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_ConstructedDataTypeDefinition  {

    private boolean referenceDatatypeSupported;
    private boolean multisetDatatypeSupported;
    private boolean cursorDatatypeSupported;
    private boolean rowDatatypeSupported;
    private boolean arrayDatatypeSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_ConstructedDataTypeDefinition(
        boolean referenceDatatypeSupported,        boolean multisetDatatypeSupported,        boolean cursorDatatypeSupported,        boolean rowDatatypeSupported,        boolean arrayDatatypeSupported    ) {
        this.referenceDatatypeSupported = referenceDatatypeSupported;
        this.multisetDatatypeSupported = multisetDatatypeSupported;
        this.cursorDatatypeSupported = cursorDatatypeSupported;
        this.rowDatatypeSupported = rowDatatypeSupported;
        this.arrayDatatypeSupported = arrayDatatypeSupported;
    }


    public boolean getReferencedatatypesupported() {
        return referenceDatatypeSupported;
    }

    public void setReferencedatatypesupported(boolean referenceDatatypeSupported) {
        this.referenceDatatypeSupported = referenceDatatypeSupported;
    }
    public boolean getMultisetdatatypesupported() {
        return multisetDatatypeSupported;
    }

    public void setMultisetdatatypesupported(boolean multisetDatatypeSupported) {
        this.multisetDatatypeSupported = multisetDatatypeSupported;
    }
    public boolean getCursordatatypesupported() {
        return cursorDatatypeSupported;
    }

    public void setCursordatatypesupported(boolean cursorDatatypeSupported) {
        this.cursorDatatypeSupported = cursorDatatypeSupported;
    }
    public boolean getRowdatatypesupported() {
        return rowDatatypeSupported;
    }

    public void setRowdatatypesupported(boolean rowDatatypeSupported) {
        this.rowDatatypeSupported = rowDatatypeSupported;
    }
    public boolean getArraydatatypesupported() {
        return arrayDatatypeSupported;
    }

    public void setArraydatatypesupported(boolean arrayDatatypeSupported) {
        this.arrayDatatypeSupported = arrayDatatypeSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}