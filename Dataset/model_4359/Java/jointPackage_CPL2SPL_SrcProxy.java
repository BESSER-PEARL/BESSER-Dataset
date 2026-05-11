





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_SrcProxy extends SrcSignallingAction {

    private String timeout;
    private String recurse;
    private String ordering;



    public jointPackage_CPL2SPL_SrcProxy(
        String timeout,        String recurse,        String ordering    ) {
        super(
        );
        this.timeout = timeout;
        this.recurse = recurse;
        this.ordering = ordering;
    }


    public String getTimeout() {
        return timeout;
    }

    public void setTimeout(String timeout) {
        this.timeout = timeout;
    }
    public String getRecurse() {
        return recurse;
    }

    public void setRecurse(String recurse) {
        this.recurse = recurse;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }


}