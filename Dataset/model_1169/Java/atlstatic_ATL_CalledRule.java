





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_CalledRule extends Rule {

    private String isEndpoint;
    private String isEntrypoint;



    public atlstatic_ATL_CalledRule(
        String isEndpoint,        String isEntrypoint    ) {
        super(
        );
        this.isEndpoint = isEndpoint;
        this.isEntrypoint = isEntrypoint;
    }


    public String getIsendpoint() {
        return isEndpoint;
    }

    public void setIsendpoint(String isEndpoint) {
        this.isEndpoint = isEndpoint;
    }
    public String getIsentrypoint() {
        return isEntrypoint;
    }

    public void setIsentrypoint(String isEntrypoint) {
        this.isEntrypoint = isEntrypoint;
    }


}