





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_RuleWithPattern extends Rule {

    private String isAbstract;
    private String isNoDefault;
    private String isRefining;



    public atlext_ATL_RuleWithPattern(
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