





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_ATL_MatchedRule extends Rule {

    private boolean isAbstract;
    private boolean isRefining;
    private boolean isNoDefault;



    public atl_n_ocl_ATL_MatchedRule(
        boolean isAbstract,        boolean isRefining,        boolean isNoDefault    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isRefining = isRefining;
        this.isNoDefault = isNoDefault;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public boolean getIsrefining() {
        return isRefining;
    }

    public void setIsrefining(boolean isRefining) {
        this.isRefining = isRefining;
    }
    public boolean getIsnodefault() {
        return isNoDefault;
    }

    public void setIsnodefault(boolean isNoDefault) {
        this.isNoDefault = isNoDefault;
    }


}