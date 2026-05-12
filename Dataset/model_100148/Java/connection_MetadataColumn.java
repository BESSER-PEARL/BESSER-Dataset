





import java.util.List;
import java.util.ArrayList;

public class connection_MetadataColumn extends record_Field, AbstractMetadataObject {

    private String originalField;
    private String originalLength;
    private String sourceType;
    private String displayField;
    private String relationshipType;
    private String relatedEntity;
    private String pattern;
    private boolean nullable;
    private String defaultValue;
    private String talendType;
    private boolean key;





    private connection_MetadataTable connection_metadatatable;




    private connection_MetadataTable connection_metadatatable;


    public connection_MetadataColumn(
        String originalField,        String originalLength,        String sourceType,        String displayField,        String relationshipType,        String relatedEntity,        String pattern,        boolean nullable,        String defaultValue,        String talendType,        boolean key    ) {
        super(
        );
        this.originalField = originalField;
        this.originalLength = originalLength;
        this.sourceType = sourceType;
        this.displayField = displayField;
        this.relationshipType = relationshipType;
        this.relatedEntity = relatedEntity;
        this.pattern = pattern;
        this.nullable = nullable;
        this.defaultValue = defaultValue;
        this.talendType = talendType;
        this.key = key;
    }


    public String getOriginalfield() {
        return originalField;
    }

    public void setOriginalfield(String originalField) {
        this.originalField = originalField;
    }
    public String getOriginallength() {
        return originalLength;
    }

    public void setOriginallength(String originalLength) {
        this.originalLength = originalLength;
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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