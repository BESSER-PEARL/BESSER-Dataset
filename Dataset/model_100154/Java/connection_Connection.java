





import java.util.List;
import java.util.ArrayList;

public class connection_Connection extends softwaredeployment_DataProvider, AbstractMetadataObject {

    private boolean ContextMode;
    private String version;
    private String ContextId;





    private connection_Metadata connection_metadata;


    public connection_Connection(
        boolean ContextMode,        String version,        String ContextId    ) {
        super(
        );
        this.ContextMode = ContextMode;
        this.version = version;
        this.ContextId = ContextId;
    }


    public boolean getContextmode() {
        return ContextMode;
    }

    public void setContextmode(boolean ContextMode) {
        this.ContextMode = ContextMode;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getContextid() {
        return ContextId;
    }

    public void setContextid(String ContextId) {
        this.ContextId = ContextId;
    }

    public connection_Metadata getConnection_metadata() {
        return connection_metadata;
    }

    public void setConnection_metadata(connection_Metadata connection_metadata) {
        this.connection_metadata = connection_metadata;
    }

}