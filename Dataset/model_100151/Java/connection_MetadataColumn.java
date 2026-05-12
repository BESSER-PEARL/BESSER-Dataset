





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataColumn extends AbstractMetadataObject {

    private String talendType;
    private String precision;
    private String sourceType;
    private String displayField;
    private boolean nullable;
    private String defaultValue;
    private boolean key;
    private String pattern;
    private String length;
    private String originalField;





    private connection_MetadataTable connection_metadatatable;




    private connection_MetadataTable connection_metadatatable;


    public connection_MetadataColumn(
        String talendType,        String precision,        String sourceType,        String displayField,        boolean nullable,        String defaultValue,        boolean key,        String pattern,        String length,        String originalField    ) {
        super(
        );
        this.talendType = talendType;
        this.precision = precision;
        this.sourceType = sourceType;
        this.displayField = displayField;
        this.nullable = nullable;
        this.defaultValue = defaultValue;
        this.key = key;
        this.pattern = pattern;
        this.length = length;
        this.originalField = originalField;
    }


    public String getTalendtype() {
        return talendType;
    }

    public void setTalendtype(String talendType) {
        this.talendType = talendType;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
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
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
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
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getOriginalfield() {
        return originalField;
    }

    public void setOriginalfield(String originalField) {
        this.originalField = originalField;
    }

    public connection_MetadataTable getConnection_metadatatable() {
        return connection_metadatatable;
    }

    public void setConnection_metadatatable(connection_MetadataTable connection_metadatatable) {
        this.connection_metadatatable = connection_metadatatable;
    }
    public connection_MetadataTable getConnection_metadatatable() {
        return connection_metadatatable;
    }

    public void setConnection_metadatatable(connection_MetadataTable connection_metadatatable) {
        this.connection_metadatatable = connection_metadatatable;
    }

}