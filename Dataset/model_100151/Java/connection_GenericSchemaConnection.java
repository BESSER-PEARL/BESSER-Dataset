





import java.util.List;
import java.util.ArrayList;

public class connection_GenericSchemaConnection extends Connection {

    private String mappingTypeId;
    private boolean mappingTypeUsed;



    public connection_GenericSchemaConnection(
        String mappingTypeId,        boolean mappingTypeUsed    ) {
        super(
        );
        this.mappingTypeId = mappingTypeId;
        this.mappingTypeUsed = mappingTypeUsed;
    }


    public String getMappingtypeid() {
        return mappingTypeId;
    }

    public void setMappingtypeid(String mappingTypeId) {
        this.mappingTypeId = mappingTypeId;
    }
    public boolean getMappingtypeused() {
        return mappingTypeUsed;
    }

    public void setMappingtypeused(boolean mappingTypeUsed) {
        this.mappingTypeUsed = mappingTypeUsed;
    }


}