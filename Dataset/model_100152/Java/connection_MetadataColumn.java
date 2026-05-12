





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataColumn extends record_Field, AbstractMetadataObject {

    private String talendType;
    private String displayField;
    private boolean key;
    private String pattern;
    private String defaultValue;
    private String originalField;
    private boolean nullable;
    private String sourceType;



    public connection_MetadataColumn(
        String talendType,        String displayField,        boolean key,        String pattern,        String defaultValue,        String originalField,        boolean nullable,        String sourceType    ) {
        super(
        );
        this.talendType = talendType;
        this.displayField = displayField;
        this.key = key;
        this.pattern = pattern;
        this.defaultValue = defaultValue;
        this.originalField = originalField;
        this.nullable = nullable;
        this.sourceType = sourceType;
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
    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
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
    public String getOriginalfield() {
        return originalField;
    }

    public void setOriginalfield(String originalField) {
        this.originalField = originalField;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getSourcetype() {
        return sourceType;
    }

    public void setSourcetype(String sourceType) {
        this.sourceType = sourceType;
    }


}