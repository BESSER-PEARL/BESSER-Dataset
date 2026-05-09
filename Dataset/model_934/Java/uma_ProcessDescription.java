





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessDescription extends ActivityDescription {

    private String usageNotes;
    private String scope;



    public uma_ProcessDescription(
        String usageNotes,        String scope    ) {
        super(
        );
        this.usageNotes = usageNotes;
        this.scope = scope;
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


}