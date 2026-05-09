





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_ATL_CalledRule extends Rule {

    private boolean isEndpoint;
    private boolean isEntrypoint;



    public atl_n_ocl_ATL_CalledRule(
        boolean isEndpoint,        boolean isEntrypoint    ) {
        super(
        );
        this.isEndpoint = isEndpoint;
        this.isEntrypoint = isEntrypoint;
    }


    public boolean getIsendpoint() {
        return isEndpoint;
    }

    public void setIsendpoint(boolean isEndpoint) {
        this.isEndpoint = isEndpoint;
    }
    public boolean getIsentrypoint() {
        return isEntrypoint;
    }

    public void setIsentrypoint(boolean isEntrypoint) {
        this.isEntrypoint = isEntrypoint;
    }


}