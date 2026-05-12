





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataColumn extends record_Field, AbstractMetadataObject {

    private String sourceType;
    private String originalField;
    private String defaultValue;
    private String pattern;
    private boolean nullable;
    private String displayField;
    private String talendType;
    private String originalLength;
    private boolean key;
    private String relationshipType;
    private String relatedEntity;





    private connection_MetadataTable connection_metadatatable;




    private connection_MetadataTable connection_metadatatable;


    public connection_MetadataColumn(
        String sourceType,        String originalField,        String defaultValue,        String pattern,        boolean nullable,        String displayField,        String talendType,        String originalLength,        boolean key,        String relationshipType,        String relatedEntity    ) {
        super(
        );
        this.sourceType = sourceType;
        this.originalField = originalField;
        this.defaultValue = defaultValue;
        this.pattern = pattern;
        this.nullable = nullable;
        this.displayField = displayField;
        this.talendType = talendType;
        this.originalLength = originalLength;
        this.key = key;
        this.relationshipType = relationshipType;
        this.relatedEntity = relatedEntity;
    }


    public String getSourcetype() {
        return sourceType;
    }

    public void setSourcetype(String sourceType) {
        this.sourceType = sourceType;
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
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
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
    public String getOriginallength() {
        return originalLength;
    }

    public void setOriginallength(String originalLength) {
        this.originalLength = originalLength;
    }
    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
    }
    public String getRelationshiptype() {
        return relationshipType;
    }

    public void setRelationshiptype(String relationshipType) {
        this.relationshipType = relationshipType;
    }
    public String getRelatedentity() {
        return relatedEntity;
    }

    public void setRelatedentity(String relatedEntity) {
        this.relatedEntity = relatedEntity;
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