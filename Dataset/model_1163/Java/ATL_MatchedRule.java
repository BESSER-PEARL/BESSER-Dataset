





import java.util.List;
import java.util.ArrayList;

public class ATL_MatchedRule extends Rule {

    private String isNoDefault;
    private String isAbstract;
    private String isRefining;



    public ATL_MatchedRule(
        String isNoDefault,        String isAbstract,        String isRefining    ) {
        super(
        );
        this.isNoDefault = isNoDefault;
        this.isAbstract = isAbstract;
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
    public String getIsrefining() {
        return isRefining;
    }

    public void setIsrefining(String isRefining) {
        this.isRefining = isRefining;
    }


}