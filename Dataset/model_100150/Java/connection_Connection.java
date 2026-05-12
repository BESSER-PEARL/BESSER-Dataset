





import java.util.List;
import java.util.ArrayList;

public class connection_Connection extends AbstractMetadataObject {

    private String version;
    private String ContextId;
    private boolean ContextMode;





    private connection_Metadata connection_metadata;


    public connection_Connection(
        String version,        String ContextId,        boolean ContextMode    ) {
        super(
        );
        this.version = version;
        this.ContextId = ContextId;
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
    public boolean getContextmode() {
        return ContextMode;
    }

    public void setContextmode(boolean ContextMode) {
        this.ContextMode = ContextMode;
    }

    public connection_Metadata getConnection_metadata() {
        return connection_metadata;
    }

    public void setConnection_metadata(connection_Metadata connection_metadata) {
        this.connection_metadata = connection_metadata;
    }

}