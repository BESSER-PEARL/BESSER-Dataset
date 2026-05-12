





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_SequenceDefinition  {

    private String noCacheString;
    private boolean cacheSupported;
    private String noMaximumValueString;
    private String noMinimumValueString;
    private int cacheDefaultValue;
    private boolean typeEnumerationSupported;
    private boolean orderSupported;





    private dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition;




    private List<dbdefinition_PredefinedDataTypeDefinition> dbdefinition_predefineddatatypedefinitions;




    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_SequenceDefinition(
        String noCacheString,        boolean cacheSupported,        String noMaximumValueString,        String noMinimumValueString,        int cacheDefaultValue,        boolean typeEnumerationSupported,        boolean orderSupported    ) {
        this.noCacheString = noCacheString;
        this.cacheSupported = cacheSupported;
        this.noMaximumValueString = noMaximumValueString;
        this.noMinimumValueString = noMinimumValueString;
        this.cacheDefaultValue = cacheDefaultValue;
        this.typeEnumerationSupported = typeEnumerationSupported;
        this.orderSupported = orderSupported;
        this.dbdefinition_predefineddatatypedefinitions = new ArrayList<>();
    }

    public dbdefinition_SequenceDefinition(
        String noCacheString,        boolean cacheSupported,        String noMaximumValueString,        String noMinimumValueString,        int cacheDefaultValue,        boolean typeEnumerationSupported,        boolean orderSupported        ArrayList<dbdefinition_PredefinedDataTypeDefinition> dbdefinition_predefineddatatypedefinitions    ) {
        this.noCacheString = noCacheString;
        this.cacheSupported = cacheSupported;
        this.noMaximumValueString = noMaximumValueString;
        this.noMinimumValueString = noMinimumValueString;
        this.cacheDefaultValue = cacheDefaultValue;
        this.typeEnumerationSupported = typeEnumerationSupported;
        this.orderSupported = orderSupported;
        this.dbdefinition_predefineddatatypedefinitions = dbdefinition_predefineddatatypedefinitions;
    }

    public String getNocachestring() {
        return noCacheString;
    }

    public void setNocachestring(String noCacheString) {
        this.noCacheString = noCacheString;
    }
    public boolean getCachesupported() {
        return cacheSupported;
    }

    public void setCachesupported(boolean cacheSupported) {
        this.cacheSupported = cacheSupported;
    }
    public String getNomaximumvaluestring() {
        return noMaximumValueString;
    }

    public void setNomaximumvaluestring(String noMaximumValueString) {
        this.noMaximumValueString = noMaximumValueString;
    }
    public String getNominimumvaluestring() {
        return noMinimumValueString;
    }

    public void setNominimumvaluestring(String noMinimumValueString) {
        this.noMinimumValueString = noMinimumValueString;
    }
    public int getCachedefaultvalue() {
        return cacheDefaultValue;
    }

    public void setCachedefaultvalue(int cacheDefaultValue) {
        this.cacheDefaultValue = cacheDefaultValue;
    }
    public boolean getTypeenumerationsupported() {
        return typeEnumerationSupported;
    }

    public void setTypeenumerationsupported(boolean typeEnumerationSupported) {
        this.typeEnumerationSupported = typeEnumerationSupported;
    }
    public boolean getOrdersupported() {
        return orderSupported;
    }

    public void setOrdersupported(boolean orderSupported) {
        this.orderSupported = orderSupported;
    }

    public dbdefinition_PredefinedDataTypeDefinition getDbdefinition_predefineddatatypedefinition() {
        return dbdefinition_predefineddatatypedefinition;
    }

    public void setDbdefinition_predefineddatatypedefinition(dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition) {
        this.dbdefinition_predefineddatatypedefinition = dbdefinition_predefineddatatypedefinition;
    }
    public List<dbdefinition_PredefinedDataTypeDefinition> getDbdefinition_predefineddatatypedefinitions() {
        return dbdefinition_predefineddatatypedefinitions;
    }

    public void addDbdefinition_predefineddatatypedefinition(Dbdefinition_predefineddatatypedefinition dbdefinition_predefineddatatypedefinition) {
        this.dbdefinition_predefineddatatypedefinitions.add(dbdefinition_predefineddatatypedefinition);
    }
    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}