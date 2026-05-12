





import java.util.List;
import java.util.ArrayList;

public class relational_Column extends RelationalEntity {

    private boolean fixedLength;
    private boolean currency;
    private int length;
    private boolean updateable;
    private String minimumValue;
    private String searchability;
    private int distinctValueCount;
    private int radix;
    private String collationName;
    private boolean selectable;
    private int scale;
    private String nullable;
    private boolean autoIncremented;
    private String nativeType;
    private String format;
    private boolean signed;
    private boolean caseSensitive;
    private int precision;
    private String defaultValue;
    private int nullValueCount;
    private String characterSetName;
    private String maximumValue;





    private List<relational_AccessPattern> relational_accesspatterns;




    private relational_AccessPattern relational_accesspattern;


    public relational_Column(
        boolean fixedLength,        boolean currency,        int length,        boolean updateable,        String minimumValue,        String searchability,        int distinctValueCount,        int radix,        String collationName,        boolean selectable,        int scale,        String nullable,        boolean autoIncremented,        String nativeType,        String format,        boolean signed,        boolean caseSensitive,        int precision,        String defaultValue,        int nullValueCount,        String characterSetName,        String maximumValue    ) {
        super(
        );
        this.fixedLength = fixedLength;
        this.currency = currency;
        this.length = length;
        this.updateable = updateable;
        this.minimumValue = minimumValue;
        this.searchability = searchability;
        this.distinctValueCount = distinctValueCount;
        this.radix = radix;
        this.collationName = collationName;
        this.selectable = selectable;
        this.scale = scale;
        this.nullable = nullable;
        this.autoIncremented = autoIncremented;
        this.nativeType = nativeType;
        this.format = format;
        this.signed = signed;
        this.caseSensitive = caseSensitive;
        this.precision = precision;
        this.defaultValue = defaultValue;
        this.nullValueCount = nullValueCount;
        this.characterSetName = characterSetName;
        this.maximumValue = maximumValue;
        this.relational_accesspatterns = new ArrayList<>();
    }

    public relational_Column(
        boolean fixedLength,        boolean currency,        int length,        boolean updateable,        String minimumValue,        String searchability,        int distinctValueCount,        int radix,        String collationName,        boolean selectable,        int scale,        String nullable,        boolean autoIncremented,        String nativeType,        String format,        boolean signed,        boolean caseSensitive,        int precision,        String defaultValue,        int nullValueCount,        String characterSetName,        String maximumValue        ArrayList<relational_AccessPattern> relational_accesspatterns    ) {
        this.fixedLength = fixedLength;
        this.currency = currency;
        this.length = length;
        this.updateable = updateable;
        this.minimumValue = minimumValue;
        this.searchability = searchability;
        this.distinctValueCount = distinctValueCount;
        this.radix = radix;
        this.collationName = collationName;
        this.selectable = selectable;
        this.scale = scale;
        this.nullable = nullable;
        this.autoIncremented = autoIncremented;
        this.nativeType = nativeType;
        this.format = format;
        this.signed = signed;
        this.caseSensitive = caseSensitive;
        this.precision = precision;
        this.defaultValue = defaultValue;
        this.nullValueCount = nullValueCount;
        this.characterSetName = characterSetName;
        this.maximumValue = maximumValue;
        this.relational_accesspatterns = relational_accesspatterns;
    }

    public boolean getFixedlength() {
        return fixedLength;
    }

    public void setFixedlength(boolean fixedLength) {
        this.fixedLength = fixedLength;
    }
    public boolean getCurrency() {
        return currency;
    }

    public void setCurrency(boolean currency) {
        this.currency = currency;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public boolean getUpdateable() {
        return updateable;
    }

    public void setUpdateable(boolean updateable) {
        this.updateable = updateable;
    }
    public String getMinimumvalue() {
        return minimumValue;
    }

    public void setMinimumvalue(String minimumValue) {
        this.minimumValue = minimumValue;
    }
    public String getSearchability() {
        return searchability;
    }

    public void setSearchability(String searchability) {
        this.searchability = searchability;
    }
    public int getDistinctvaluecount() {
        return distinctValueCount;
    }

    public void setDistinctvaluecount(int distinctValueCount) {
        this.distinctValueCount = distinctValueCount;
    }
    public int getRadix() {
        return radix;
    }

    public void setRadix(int radix) {
        this.radix = radix;
    }
    public String getCollationname() {
        return collationName;
    }

    public void setCollationname(String collationName) {
        this.collationName = collationName;
    }
    public boolean getSelectable() {
        return selectable;
    }

    public void setSelectable(boolean selectable) {
        this.selectable = selectable;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public String getNullable() {
        return nullable;
    }

    public void setNullable(String nullable) {
        this.nullable = nullable;
    }
    public boolean getAutoincremented() {
        return autoIncremented;
    }

    public void setAutoincremented(boolean autoIncremented) {
        this.autoIncremented = autoIncremented;
    }
    public String getNativetype() {
        return nativeType;
    }

    public void setNativetype(String nativeType) {
        this.nativeType = nativeType;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public boolean getSigned() {
        return signed;
    }

    public void setSigned(boolean signed) {
        this.signed = signed;
    }
    public boolean getCasesensitive() {
        return caseSensitive;
    }

    public void setCasesensitive(boolean caseSensitive) {
        this.caseSensitive = caseSensitive;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public int getNullvaluecount() {
        return nullValueCount;
    }

    public void setNullvaluecount(int nullValueCount) {
        this.nullValueCount = nullValueCount;
    }
    public String getCharactersetname() {
        return characterSetName;
    }

    public void setCharactersetname(String characterSetName) {
        this.characterSetName = characterSetName;
    }
    public String getMaximumvalue() {
        return maximumValue;
    }

    public void setMaximumvalue(String maximumValue) {
        this.maximumValue = maximumValue;
    }

    public List<relational_AccessPattern> getRelational_accesspatterns() {
        return relational_accesspatterns;
    }

    public void addRelational_accesspattern(Relational_accesspattern relational_accesspattern) {
        this.relational_accesspatterns.add(relational_accesspattern);
    }
    public relational_AccessPattern getRelational_accesspattern() {
        return relational_accesspattern;
    }

    public void setRelational_accesspattern(relational_AccessPattern relational_accesspattern) {
        this.relational_accesspattern = relational_accesspattern;
    }

}