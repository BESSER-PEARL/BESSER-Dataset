





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataColumn  {

    private String sourceType;
    private String pattern;
    private String defaultValue;
    private boolean key;
    private String originalField;
    private String talendType;
    private String displayField;
    private boolean nullable;



    public connection_MetadataColumn(
        String sourceType,        String pattern,        String defaultValue,        boolean key,        String originalField,        String talendType,        String displayField,        boolean nullable    ) {
        this.sourceType = sourceType;
        this.pattern = pattern;
        this.defaultValue = defaultValue;
        this.key = key;
        this.originalField = originalField;
        this.talendType = talendType;
        this.displayField = displayField;
        this.nullable = nullable;
    }


    public String getSourcetype() {
        return sourceType;
    }

    public void setSourcetype(String sourceType) {
        this.sourceType = sourceType;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
    }
    public String getOriginalfield() {
        return originalField;
    }

    public void setOriginalfield(String originalField) {
        this.originalField = originalField;
    }
    public String getTalendtype() {
        return talendType;
    }

    public void setTalendtype(String talendType) {
        this.talendType = talendType;
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


}