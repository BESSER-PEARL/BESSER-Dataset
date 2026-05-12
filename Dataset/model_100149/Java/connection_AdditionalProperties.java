





import java.util.List;
import java.util.ArrayList;

public class connection_AdditionalProperties  {

    private String key;
    private String value;





    private connection_MetadataTable connection_metadatatable;


    public connection_AdditionalProperties(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public connection_MetadataTable getConnection_metadatatable() {
        return connection_metadatatable;
    }

    public void setConnection_metadatatable(connection_MetadataTable connection_metadatatable) {
        this.connection_metadatatable = connection_metadatatable;
    }

}