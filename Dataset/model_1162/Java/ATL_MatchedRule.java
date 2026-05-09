





import java.util.List;
import java.util.ArrayList;

public class ATL_MatchedRule extends Rule {

    private String isAbstract;
    private String isNoDefault;
    private String isRefining;



    public ATL_MatchedRule(
        String isAbstract,        String isNoDefault,        String isRefining    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isNoDefault = isNoDefault;
        this.isRefining = isRefining;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
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


}