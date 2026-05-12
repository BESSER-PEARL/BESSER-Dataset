





import java.util.List;
import java.util.ArrayList;

public class connection_Connection extends AbstractMetadataObject {

    private String ContextId;
    private String version;
    private boolean ContextMode;



    public connection_Connection(
        String ContextId,        String version,        boolean ContextMode    ) {
        super(
        );
        this.ContextId = ContextId;
        this.version = version;
        this.ContextMode = ContextMode;
    }


    public String getContextid() {
        return ContextId;
    }

    public void setContextid(String ContextId) {
        this.ContextId = ContextId;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getContextmode() {
        return ContextMode;
    }

    public void setContextmode(boolean ContextMode) {
        this.ContextMode = ContextMode;
    }


}