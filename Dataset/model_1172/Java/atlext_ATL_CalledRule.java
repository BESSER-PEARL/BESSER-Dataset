





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_CalledRule extends StaticRule {

    private String isEntrypoint;
    private String isEndpoint;



    public atlext_ATL_CalledRule(
        String isEntrypoint,        String isEndpoint    ) {
        super(
        );
        this.isEntrypoint = isEntrypoint;
        this.isEndpoint = isEndpoint;
    }


    public String getIsentrypoint() {
        return isEntrypoint;
    }

    public void setIsentrypoint(String isEntrypoint) {
        this.isEntrypoint = isEntrypoint;
    }
    public String getIsendpoint() {
        return isEndpoint;
    }

    public void setIsendpoint(String isEndpoint) {
        this.isEndpoint = isEndpoint;
    }


}