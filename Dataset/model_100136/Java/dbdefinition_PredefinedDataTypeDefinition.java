





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_PredefinedDataTypeDefinition  {

    private boolean lengthSupported;
    private int cutoffPrecision;
    private String primitiveType;
    private boolean groupingSupported;
    private boolean clusteringSupported;
    private int defaultLength;
    private boolean keyConstraintSupported;
    private boolean defaultSupported;
    private String name;
    private String maximumValue;
    private String lengthSemantic;
    private String minimumValue;
    private boolean largeValueSpecifierSupported;
    private boolean bitDataSupported;
    private boolean displayNameSupported;
    private int maximumLength;
    private int defaultScale;
    private boolean precisionSupported;
    private int largeValueSpecifierLength;
    private boolean scaleSupported;
    private String encodingScheme;
    private int jdbcEnumType;
    private boolean orderingSupported;
    private String defaultValueTypes;
    private String characterSet;
    private int defaultPrecision;
    private String displayName;
    private boolean trailingFieldQualifierSupported;
    private String languageType;
    private boolean lengthSemanticSupported;
    private boolean fillFactorSupported;
    private String fieldQualifierSeparator;
    private int maximumPrecision;
    private boolean leadingFieldQualifierSupported;
    private int maximumScale;
    private String lengthUnit;
    private boolean multipleColumnsSupported;
    private int minimumScale;
    private String javaClassName;
    private boolean nullableSupported;
    private String characterSetSuffix;
    private boolean identitySupported;
    private String encodingSchemeSuffix;
    private String largeValueSpecifierName;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_PredefinedDataTypeDefinition(
        boolean lengthSupported,        int cutoffPrecision,        String primitiveType,        boolean groupingSupported,        boolean clusteringSupported,        int defaultLength,        boolean keyConstraintSupported,        boolean defaultSupported,        String name,        String maximumValue,        String lengthSemantic,        String minimumValue,        boolean largeValueSpecifierSupported,        boolean bitDataSupported,        boolean displayNameSupported,        int maximumLength,        int defaultScale,        boolean precisionSupported,        int largeValueSpecifierLength,        boolean scaleSupported,        String encodingScheme,        int jdbcEnumType,        boolean orderingSupported,        String defaultValueTypes,        String characterSet,        int defaultPrecision,        String displayName,        boolean trailingFieldQualifierSupported,        String languageType,        boolean lengthSemanticSupported,        boolean fillFactorSupported,        String fieldQualifierSeparator,        int maximumPrecision,        boolean leadingFieldQualifierSupported,        int maximumScale,        String lengthUnit,        boolean multipleColumnsSupported,        int minimumScale,        String javaClassName,        boolean nullableSupported,        String characterSetSuffix,        boolean identitySupported,        String encodingSchemeSuffix,        String largeValueSpecifierName    ) {
        this.lengthSupported = lengthSupported;
        this.cutoffPrecision = cutoffPrecision;
        this.primitiveType = primitiveType;
        this.groupingSupported = groupingSupported;
        this.clusteringSupported = clusteringSupported;
        this.defaultLength = defaultLength;
        this.keyConstraintSupported = keyConstraintSupported;
        this.defaultSupported = defaultSupported;
        this.name = name;
        this.maximumValue = maximumValue;
        this.lengthSemantic = lengthSemantic;
        this.minimumValue = minimumValue;
        this.largeValueSpecifierSupported = largeValueSpecifierSupported;
        this.bitDataSupported = bitDataSupported;
        this.displayNameSupported = displayNameSupported;
        this.maximumLength = maximumLength;
        this.defaultScale = defaultScale;
        this.precisionSupported = precisionSupported;
        this.largeValueSpecifierLength = largeValueSpecifierLength;
        this.scaleSupported = scaleSupported;
        this.encodingScheme = encodingScheme;
        this.jdbcEnumType = jdbcEnumType;
        this.orderingSupported = orderingSupported;
        this.defaultValueTypes = defaultValueTypes;
        this.characterSet = characterSet;
        this.defaultPrecision = defaultPrecision;
        this.displayName = displayName;
        this.trailingFieldQualifierSupported = trailingFieldQualifierSupported;
        this.languageType = languageType;
        this.lengthSemanticSupported = lengthSemanticSupported;
        this.fillFactorSupported = fillFactorSupported;
        this.fieldQualifierSeparator = fieldQualifierSeparator;
        this.maximumPrecision = maximumPrecision;
        this.leadingFieldQualifierSupported = leadingFieldQualifierSupported;
        this.maximumScale = maximumScale;
        this.lengthUnit = lengthUnit;
        this.multipleColumnsSupported = multipleColumnsSupported;
        this.minimumScale = minimumScale;
        this.javaClassName = javaClassName;
        this.nullableSupported = nullableSupported;
        this.characterSetSuffix = characterSetSuffix;
        this.identitySupported = identitySupported;
        this.encodingSchemeSuffix = encodingSchemeSuffix;
        this.largeValueSpecifierName = largeValueSpecifierName;
    }


    public boolean getLengthsupported() {
        return lengthSupported;
    }

    public void setLengthsupported(boolean lengthSupported) {
        this.lengthSupported = lengthSupported;
    }
    public int getCutoffprecision() {
        return cutoffPrecision;
    }

    public void setCutoffprecision(int cutoffPrecision) {
        this.cutoffPrecision = cutoffPrecision;
    }
    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }
    public boolean getGroupingsupported() {
        return groupingSupported;
    }

    public void setGroupingsupported(boolean groupingSupported) {
        this.groupingSupported = groupingSupported;
    }
    public boolean getClusteringsupported() {
        return clusteringSupported;
    }

    public void setClusteringsupported(boolean clusteringSupported) {
        this.clusteringSupported = clusteringSupported;
    }
    public int getDefaultlength() {
        return defaultLength;
    }

    public void setDefaultlength(int defaultLength) {
        this.defaultLength = defaultLength;
    }
    public boolean getKeyconstraintsupported() {
        return keyConstraintSupported;
    }

    public void setKeyconstraintsupported(boolean keyConstraintSupported) {
        this.keyConstraintSupported = keyConstraintSupported;
    }
    public boolean getDefaultsupported() {
        return defaultSupported;
    }

    public void setDefaultsupported(boolean defaultSupported) {
        this.defaultSupported = defaultSupported;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMaximumvalue() {
        return maximumValue;
    }

    public void setMaximumvalue(String maximumValue) {
        this.maximumValue = maximumValue;
    }
    public String getLengthsemantic() {
        return lengthSemantic;
    }

    public void setLengthsemantic(String lengthSemantic) {
        this.lengthSemantic = lengthSemantic;
    }
    public String getMinimumvalue() {
        return minimumValue;
    }

    public void setMinimumvalue(String minimumValue) {
        this.minimumValue = minimumValue;
    }
    public boolean getLargevaluespecifiersupported() {
        return largeValueSpecifierSupported;
    }

    public void setLargevaluespecifiersupported(boolean largeValueSpecifierSupported) {
        this.largeValueSpecifierSupported = largeValueSpecifierSupported;
    }
    public boolean getBitdatasupported() {
        return bitDataSupported;
    }

    public void setBitdatasupported(boolean bitDataSupported) {
        this.bitDataSupported = bitDataSupported;
    }
    public boolean getDisplaynamesupported() {
        return displayNameSupported;
    }

    public void setDisplaynamesupported(boolean displayNameSupported) {
        this.displayNameSupported = displayNameSupported;
    }
    public int getMaximumlength() {
        return maximumLength;
    }

    public void setMaximumlength(int maximumLength) {
        this.maximumLength = maximumLength;
    }
    public int getDefaultscale() {
        return defaultScale;
    }

    public void setDefaultscale(int defaultScale) {
        this.defaultScale = defaultScale;
    }
    public boolean getPrecisionsupported() {
        return precisionSupported;
    }

    public void setPrecisionsupported(boolean precisionSupported) {
        this.precisionSupported = precisionSupported;
    }
    public int getLargevaluespecifierlength() {
        return largeValueSpecifierLength;
    }

    public void setLargevaluespecifierlength(int largeValueSpecifierLength) {
        this.largeValueSpecifierLength = largeValueSpecifierLength;
    }
    public boolean getScalesupported() {
        return scaleSupported;
    }

    public void setScalesupported(boolean scaleSupported) {
        this.scaleSupported = scaleSupported;
    }
    public String getEncodingscheme() {
        return encodingScheme;
    }

    public void setEncodingscheme(String encodingScheme) {
        this.encodingScheme = encodingScheme;
    }
    public int getJdbcenumtype() {
        return jdbcEnumType;
    }

    public void setJdbcenumtype(int jdbcEnumType) {
        this.jdbcEnumType = jdbcEnumType;
    }
    public boolean getOrderingsupported() {
        return orderingSupported;
    }

    public void setOrderingsupported(boolean orderingSupported) {
        this.orderingSupported = orderingSupported;
    }
    public String getDefaultvaluetypes() {
        return defaultValueTypes;
    }

    public void setDefaultvaluetypes(String defaultValueTypes) {
        this.defaultValueTypes = defaultValueTypes;
    }
    public String getCharacterset() {
        return characterSet;
    }

    public void setCharacterset(String characterSet) {
        this.characterSet = characterSet;
    }
    public int getDefaultprecision() {
        return defaultPrecision;
    }

    public void setDefaultprecision(int defaultPrecision) {
        this.defaultPrecision = defaultPrecision;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public boolean getTrailingfieldqualifiersupported() {
        return trailingFieldQualifierSupported;
    }

    public void setTrailingfieldqualifiersupported(boolean trailingFieldQualifierSupported) {
        this.trailingFieldQualifierSupported = trailingFieldQualifierSupported;
    }
    public String getLanguagetype() {
        return languageType;
    }

    public void setLanguagetype(String languageType) {
        this.languageType = languageType;
    }
    public boolean getLengthsemanticsupported() {
        return lengthSemanticSupported;
    }

    public void setLengthsemanticsupported(boolean lengthSemanticSupported) {
        this.lengthSemanticSupported = lengthSemanticSupported;
    }
    public boolean getFillfactorsupported() {
        return fillFactorSupported;
    }

    public void setFillfactorsupported(boolean fillFactorSupported) {
        this.fillFactorSupported = fillFactorSupported;
    }
    public String getFieldqualifierseparator() {
        return fieldQualifierSeparator;
    }

    public void setFieldqualifierseparator(String fieldQualifierSeparator) {
        this.fieldQualifierSeparator = fieldQualifierSeparator;
    }
    public int getMaximumprecision() {
        return maximumPrecision;
    }

    public void setMaximumprecision(int maximumPrecision) {
        this.maximumPrecision = maximumPrecision;
    }
    public boolean getLeadingfieldqualifiersupported() {
        return leadingFieldQualifierSupported;
    }

    public void setLeadingfieldqualifiersupported(boolean leadingFieldQualifierSupported) {
        this.leadingFieldQualifierSupported = leadingFieldQualifierSupported;
    }
    public int getMaximumscale() {
        return maximumScale;
    }

    public void setMaximumscale(int maximumScale) {
        this.maximumScale = maximumScale;
    }
    public String getLengthunit() {
        return lengthUnit;
    }

    public void setLengthunit(String lengthUnit) {
        this.lengthUnit = lengthUnit;
    }
    public boolean getMultiplecolumnssupported() {
        return multipleColumnsSupported;
    }

    public void setMultiplecolumnssupported(boolean multipleColumnsSupported) {
        this.multipleColumnsSupported = multipleColumnsSupported;
    }
    public int getMinimumscale() {
        return minimumScale;
    }

    public void setMinimumscale(int minimumScale) {
        this.minimumScale = minimumScale;
    }
    public String getJavaclassname() {
        return javaClassName;
    }

    public void setJavaclassname(String javaClassName) {
        this.javaClassName = javaClassName;
    }
    public boolean getNullablesupported() {
        return nullableSupported;
    }

    public void setNullablesupported(boolean nullableSupported) {
        this.nullableSupported = nullableSupported;
    }
    public String getCharactersetsuffix() {
        return characterSetSuffix;
    }

    public void setCharactersetsuffix(String characterSetSuffix) {
        this.characterSetSuffix = characterSetSuffix;
    }
    public boolean getIdentitysupported() {
        return identitySupported;
    }

    public void setIdentitysupported(boolean identitySupported) {
        this.identitySupported = identitySupported;
    }
    public String getEncodingschemesuffix() {
        return encodingSchemeSuffix;
    }

    public void setEncodingschemesuffix(String encodingSchemeSuffix) {
        this.encodingSchemeSuffix = encodingSchemeSuffix;
    }
    public String getLargevaluespecifiername() {
        return largeValueSpecifierName;
    }

    public void setLargevaluespecifiername(String largeValueSpecifierName) {
        this.largeValueSpecifierName = largeValueSpecifierName;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}