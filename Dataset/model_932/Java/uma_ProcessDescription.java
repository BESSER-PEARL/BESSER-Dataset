





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessDescription extends ActivityDescription {

    private String usageNotes;
    private String scope;
    private String externalId;



    public uma_ProcessDescription(
        String usageNotes,        String scope,        String externalId    ) {
        super(
        );
        this.usageNotes = usageNotes;
        this.scope = scope;
        this.externalId = externalId;
    }


    public String getUsagenotes() {
        return usageNotes;
    }

    public void setUsagenotes(String usageNotes) {
        this.usageNotes = usageNotes;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getExternalid() {
        return externalId;
    }

    public void setExternalid(String externalId) {
        this.externalId = externalId;
    }


}