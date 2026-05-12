





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_StoredProcedureDefinition  {

    private boolean parameterInitValueSupported;
    private boolean nullInputActionSupported;
    private boolean returnTypeSupported;
    private boolean determininsticSupported;
    private int maximumActionBodyLength;
    private String languageType;
    private boolean parameterDeclarationConstraintSupported;
    private boolean parameterStyleSupported;
    private boolean returnedTypeDeclarationConstraintSupported;
    private String functionLanguageType;
    private boolean returnedNullSupported;
    private String procedureType;
    private boolean packageGenerationSupported;
    private String parameterStyle;
    private int maximumIdentifierLength;





    private List<dbdefinition_PredefinedDataTypeDefinition> dbdefinition_predefineddatatypedefinitions;




    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_StoredProcedureDefinition(
        boolean parameterInitValueSupported,        boolean nullInputActionSupported,        boolean returnTypeSupported,        boolean determininsticSupported,        int maximumActionBodyLength,        String languageType,        boolean parameterDeclarationConstraintSupported,        boolean parameterStyleSupported,        boolean returnedTypeDeclarationConstraintSupported,        String functionLanguageType,        boolean returnedNullSupported,        String procedureType,        boolean packageGenerationSupported,        String parameterStyle,        int maximumIdentifierLength    ) {
        this.parameterInitValueSupported = parameterInitValueSupported;
        this.nullInputActionSupported = nullInputActionSupported;
        this.returnTypeSupported = returnTypeSupported;
        this.determininsticSupported = determininsticSupported;
        this.maximumActionBodyLength = maximumActionBodyLength;
        this.languageType = languageType;
        this.parameterDeclarationConstraintSupported = parameterDeclarationConstraintSupported;
        this.parameterStyleSupported = parameterStyleSupported;
        this.returnedTypeDeclarationConstraintSupported = returnedTypeDeclarationConstraintSupported;
        this.functionLanguageType = functionLanguageType;
        this.returnedNullSupported = returnedNullSupported;
        this.procedureType = procedureType;
        this.packageGenerationSupported = packageGenerationSupported;
        this.parameterStyle = parameterStyle;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.dbdefinition_predefineddatatypedefinitions = new ArrayList<>();
    }

    public dbdefinition_StoredProcedureDefinition(
        boolean parameterInitValueSupported,        boolean nullInputActionSupported,        boolean returnTypeSupported,        boolean determininsticSupported,        int maximumActionBodyLength,        String languageType,        boolean parameterDeclarationConstraintSupported,        boolean parameterStyleSupported,        boolean returnedTypeDeclarationConstraintSupported,        String functionLanguageType,        boolean returnedNullSupported,        String procedureType,        boolean packageGenerationSupported,        String parameterStyle,        int maximumIdentifierLength        ArrayList<dbdefinition_PredefinedDataTypeDefinition> dbdefinition_predefineddatatypedefinitions    ) {
        this.parameterInitValueSupported = parameterInitValueSupported;
        this.nullInputActionSupported = nullInputActionSupported;
        this.returnTypeSupported = returnTypeSupported;
        this.determininsticSupported = determininsticSupported;
        this.maximumActionBodyLength = maximumActionBodyLength;
        this.languageType = languageType;
        this.parameterDeclarationConstraintSupported = parameterDeclarationConstraintSupported;
        this.parameterStyleSupported = parameterStyleSupported;
        this.returnedTypeDeclarationConstraintSupported = returnedTypeDeclarationConstraintSupported;
        this.functionLanguageType = functionLanguageType;
        this.returnedNullSupported = returnedNullSupported;
        this.procedureType = procedureType;
        this.packageGenerationSupported = packageGenerationSupported;
        this.parameterStyle = parameterStyle;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.dbdefinition_predefineddatatypedefinitions = dbdefinition_predefineddatatypedefinitions;
    }

    public boolean getParameterinitvaluesupported() {
        return parameterInitValueSupported;
    }

    public void setParameterinitvaluesupported(boolean parameterInitValueSupported) {
        this.parameterInitValueSupported = parameterInitValueSupported;
    }
    public boolean getNullinputactionsupported() {
        return nullInputActionSupported;
    }

    public void setNullinputactionsupported(boolean nullInputActionSupported) {
        this.nullInputActionSupported = nullInputActionSupported;
    }
    public boolean getReturntypesupported() {
        return returnTypeSupported;
    }

    public void setReturntypesupported(boolean returnTypeSupported) {
        this.returnTypeSupported = returnTypeSupported;
    }
    public boolean getDetermininsticsupported() {
        return determininsticSupported;
    }

    public void setDetermininsticsupported(boolean determininsticSupported) {
        this.determininsticSupported = determininsticSupported;
    }
    public int getMaximumactionbodylength() {
        return maximumActionBodyLength;
    }

    public void setMaximumactionbodylength(int maximumActionBodyLength) {
        this.maximumActionBodyLength = maximumActionBodyLength;
    }
    public String getLanguagetype() {
        return languageType;
    }

    public void setLanguagetype(String languageType) {
        this.languageType = languageType;
    }
    public boolean getParameterdeclarationconstraintsupported() {
        return parameterDeclarationConstraintSupported;
    }

    public void setParameterdeclarationconstraintsupported(boolean parameterDeclarationConstraintSupported) {
        this.parameterDeclarationConstraintSupported = parameterDeclarationConstraintSupported;
    }
    public boolean getParameterstylesupported() {
        return parameterStyleSupported;
    }

    public void setParameterstylesupported(boolean parameterStyleSupported) {
        this.parameterStyleSupported = parameterStyleSupported;
    }
    public boolean getReturnedtypedeclarationconstraintsupported() {
        return returnedTypeDeclarationConstraintSupported;
    }

    public void setReturnedtypedeclarationconstraintsupported(boolean returnedTypeDeclarationConstraintSupported) {
        this.returnedTypeDeclarationConstraintSupported = returnedTypeDeclarationConstraintSupported;
    }
    public String getFunctionlanguagetype() {
        return functionLanguageType;
    }

    public void setFunctionlanguagetype(String functionLanguageType) {
        this.functionLanguageType = functionLanguageType;
    }
    public boolean getReturnednullsupported() {
        return returnedNullSupported;
    }

    public void setReturnednullsupported(boolean returnedNullSupported) {
        this.returnedNullSupported = returnedNullSupported;
    }
    public String getProceduretype() {
        return procedureType;
    }

    public void setProceduretype(String procedureType) {
        this.procedureType = procedureType;
    }
    public boolean getPackagegenerationsupported() {
        return packageGenerationSupported;
    }

    public void setPackagegenerationsupported(boolean packageGenerationSupported) {
        this.packageGenerationSupported = packageGenerationSupported;
    }
    public String getParameterstyle() {
        return parameterStyle;
    }

    public void setParameterstyle(String parameterStyle) {
        this.parameterStyle = parameterStyle;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
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