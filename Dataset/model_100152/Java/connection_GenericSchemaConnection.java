





import java.util.List;
import java.util.ArrayList;

public class connection_GenericSchemaConnection extends Connection {

    private boolean mappingTypeUsed;
    private String mappingTypeId;



    public connection_GenericSchemaConnection(
        boolean mappingTypeUsed,        String mappingTypeId    ) {
        super(
        );
        this.mappingTypeUsed = mappingTypeUsed;
        this.mappingTypeId = mappingTypeId;
    }


    public boolean getMappingtypeused() {
        return mappingTypeUsed;
    }

    public void setMappingtypeused(boolean mappingTypeUsed) {
        this.mappingTypeUsed = mappingTypeUsed;
    }
    public String getMappingtypeid() {
        return mappingTypeId;
    }

    public void setMappingtypeid(String mappingTypeId) {
        this.mappingTypeId = mappingTypeId;
    }


}