





import java.util.List;
import java.util.ArrayList;

public class top_ATL_MatchedRule extends Rule {

    private String isRefining;
    private String isNoDefault;
    private String isAbstract;



    public top_ATL_MatchedRule(
        String isRefining,        String isNoDefault,        String isAbstract    ) {
        super(
        );
        this.isRefining = isRefining;
        this.isNoDefault = isNoDefault;
        this.isAbstract = isAbstract;
    }


    public String getIsrefining() {
        return isRefining;
    }

    public void setIsrefining(String isRefining) {
        this.isRefining = isRefining;
    }
    public String getIsnodefault() {
        return isNoDefault;
    }

    public void setIsnodefault(String isNoDefault) {
        this.isNoDefault = isNoDefault;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}