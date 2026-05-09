





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Process extends Activity {

    private String usageNote;
    private String scope;



    public spem_uma_Process(
        String usageNote,        String scope    ) {
        super(
        );
        this.usageNote = usageNote;
        this.scope = scope;
    }


    public String getUsagenote() {
        return usageNote;
    }

    public void setUsagenote(String usageNote) {
        this.usageNote = usageNote;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}