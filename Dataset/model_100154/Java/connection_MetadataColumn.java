





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataColumn extends record_Field, AbstractMetadataObject {

    private boolean nullable;
    private String originalField;
    private String defaultValue;
    private String pattern;
    private String sourceType;
    private String displayField;
    private String talendType;
    private boolean key;



    public connection_MetadataColumn(
        boolean nullable,        String originalField,        String defaultValue,        String pattern,        String sourceType,        String displayField,        String talendType,        boolean key    ) {
        super(
        );
        this.nullable = nullable;
        this.originalField = originalField;
        this.defaultValue = defaultValue;
        this.pattern = pattern;
        this.sourceType = sourceType;
        this.displayField = displayField;
        this.talendType = talendType;
        this.key = key;
    }


    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getOriginalfield() {
        return originalField;
    }

    public void setOriginalfield(String originalField) {
        this.originalField = originalField;
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
    public String getDisplayfield() {
        return displayField;
    }

    public void setDisplayfield(String displayField) {
        this.displayField = displayField;
    }
    public String getTalendtype() {
        return talendType;
    }

    public void setTalendtype(String talendType) {
        this.talendType = talendType;
    }
    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
    }


}