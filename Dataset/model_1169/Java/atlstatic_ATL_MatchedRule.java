





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_MatchedRule extends Rule {

    private String isNoDefault;
    private String isRefining;
    private String isAbstract;



    public atlstatic_ATL_MatchedRule(
        String isNoDefault,        String isRefining,        String isAbstract    ) {
        super(
        );
        this.isNoDefault = isNoDefault;
        this.isRefining = isRefining;
        this.isAbstract = isAbstract;
    }


    public String getIsnodefault() {
        return isNoDefault;
    }

    public void setIsnodefault(String isNoDefault) {
        this.isNoDefault = isNoDefault;
    }
    public String getIsrefining() {
        return isRefining;
    }

    public void setIsrefining(String isRefining) {
        this.isRefining = isRefining;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}