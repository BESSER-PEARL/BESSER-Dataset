





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessDescription extends ActivityDescription {

    private String scope;
    private String usageNotes;
    private String externalId;



    public uma_ProcessDescription(
        String scope,        String usageNotes,        String externalId    ) {
        super(
        );
        this.scope = scope;
        this.usageNotes = usageNotes;
        this.externalId = externalId;
    }


    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getUsagenotes() {
        return usageNotes;
    }

    public void setUsagenotes(String usageNotes) {
        this.usageNotes = usageNotes;
    }
    public String getExternalid() {
        return externalId;
    }

    public void setExternalid(String externalId) {
        this.externalId = externalId;
    }


}