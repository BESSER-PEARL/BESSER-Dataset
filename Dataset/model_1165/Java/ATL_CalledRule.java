





import java.util.List;
import java.util.ArrayList;

public class ATL_CalledRule extends Rule {

    private String isEntrypoint;
    private String isEndpoint;



    public ATL_CalledRule(
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