





import java.util.List;
import java.util.ArrayList;

public class smm_ObservationScope extends SmmElement {

    private String scopeUri;



    public smm_ObservationScope(
        String scopeUri    ) {
        super(
        );
        this.scopeUri = scopeUri;
    }


    public String getScopeuri() {
        return scopeUri;
    }

    public void setScopeuri(String scopeUri) {
        this.scopeUri = scopeUri;
    }


}