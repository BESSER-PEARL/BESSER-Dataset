





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataColumn extends AbstractMetadataObject {

    private String displayField;
    private boolean nullable;
    private int length;
    private String defaultValue;
    private String pattern;
    private String sourceType;
    private boolean key;
    private String talendType;
    private int precision;
    private String originalField;



    public connection_MetadataColumn(
        String displayField,        boolean nullable,        int length,        String defaultValue,        String pattern,        String sourceType,        boolean key,        String talendType,        int precision,        String originalField    ) {
        super(
        );
        this.displayField = displayField;
        this.nullable = nullable;
        this.length = length;
        this.defaultValue = defaultValue;
        this.pattern = pattern;
        this.sourceType = sourceType;
        this.key = key;
        this.talendType = talendType;
        this.precision = precision;
        this.originalField = originalField;
    }


    public String getDisplayfield() {
        return displayField;
    }

    public void setDisplayfield(String displayField) {
        this.displayField = displayField;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getSourcetype() {
        return sourceType;
    }

    public void setSourcetype(String sourceType) {
        this.sourceType = sourceType;
    }
    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
    }
    public String getTalendtype() {
        return talendType;
    }

    public void setTalendtype(String talendType) {
        this.talendType = talendType;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public String getOriginalfield() {
        return originalField;
    }

    public void setOriginalfield(String originalField) {
        this.originalField = originalField;
    }


}