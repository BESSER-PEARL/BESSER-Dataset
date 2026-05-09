





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessDescription extends ActivityDescription {

    private String scope;
    private String usageNotes;



    public uma_ProcessDescription(
        String scope,        String usageNotes    ) {
        super(
        );
        this.scope = scope;
        this.usageNotes = usageNotes;
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


}