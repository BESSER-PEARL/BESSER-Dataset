





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_FieldQualifierDefinition  {

    private int defaultScale;
    private int maximumScale;
    private boolean scaleSupported;
    private int maximumPrecision;
    private int defaultPrecision;
    private boolean precisionSupported;
    private String name;





    private dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition;




    private dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition;




    private dbdefinition_FieldQualifierDefinition dbdefinition_fieldqualifierdefinition;




    private dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition;




    private dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition;


    public dbdefinition_FieldQualifierDefinition(
        int defaultScale,        int maximumScale,        boolean scaleSupported,        int maximumPrecision,        int defaultPrecision,        boolean precisionSupported,        String name    ) {
        this.defaultScale = defaultScale;
        this.maximumScale = maximumScale;
        this.scaleSupported = scaleSupported;
        this.maximumPrecision = maximumPrecision;
        this.defaultPrecision = defaultPrecision;
        this.precisionSupported = precisionSupported;
        this.name = name;
    }


    public int getDefaultscale() {
        return defaultScale;
    }

    public void setDefaultscale(int defaultScale) {
        this.defaultScale = defaultScale;
    }
    public int getMaximumscale() {
        return maximumScale;
    }

    public void setMaximumscale(int maximumScale) {
        this.maximumScale = maximumScale;
    }
    public boolean getScalesupported() {
        return scaleSupported;
    }

    public void setScalesupported(boolean scaleSupported) {
        this.scaleSupported = scaleSupported;
    }
    public int getMaximumprecision() {
        return maximumPrecision;
    }

    public void setMaximumprecision(int maximumPrecision) {
        this.maximumPrecision = maximumPrecision;
    }
    public int getDefaultprecision() {
        return defaultPrecision;
    }

    public void setDefaultprecision(int defaultPrecision) {
        this.defaultPrecision = defaultPrecision;
    }
    public boolean getPrecisionsupported() {
        return precisionSupported;
    }

    public void setPrecisionsupported(boolean precisionSupported) {
        this.precisionSupported = precisionSupported;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dbdefinition_PredefinedDataTypeDefinition getDbdefinition_predefineddatatypedefinition() {
        return dbdefinition_predefineddatatypedefinition;
    }

    public void setDbdefinition_predefineddatatypedefinition(dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition) {
        this.dbdefinition_predefineddatatypedefinition = dbdefinition_predefineddatatypedefinition;
    }
    public dbdefinition_PredefinedDataTypeDefinition getDbdefinition_predefineddatatypedefinition() {
        return dbdefinition_predefineddatatypedefinition;
    }

    public void setDbdefinition_predefineddatatypedefinition(dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition) {
        this.dbdefinition_predefineddatatypedefinition = dbdefinition_predefineddatatypedefinition;
    }
    public dbdefinition_FieldQualifierDefinition getDbdefinition_fieldqualifierdefinition() {
        return dbdefinition_fieldqualifierdefinition;
    }

    public void setDbdefinition_fieldqualifierdefinition(dbdefinition_FieldQualifierDefinition dbdefinition_fieldqualifierdefinition) {
        this.dbdefinition_fieldqualifierdefinition = dbdefinition_fieldqualifierdefinition;
    }
    public dbdefinition_PredefinedDataTypeDefinition getDbdefinition_predefineddatatypedefinition() {
        return dbdefinition_predefineddatatypedefinition;
    }

    public void setDbdefinition_predefineddatatypedefinition(dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition) {
        this.dbdefinition_predefineddatatypedefinition = dbdefinition_predefineddatatypedefinition;
    }
    public dbdefinition_PredefinedDataTypeDefinition getDbdefinition_predefineddatatypedefinition() {
        return dbdefinition_predefineddatatypedefinition;
    }

    public void setDbdefinition_predefineddatatypedefinition(dbdefinition_PredefinedDataTypeDefinition dbdefinition_predefineddatatypedefinition) {
        this.dbdefinition_predefineddatatypedefinition = dbdefinition_predefineddatatypedefinition;
    }

}