





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_RuleWithPattern extends Rule {

    private String isAbstract;
    private String isRefining;
    private String isNoDefault;



    public atlstatic_ATL_RuleWithPattern(
        String isAbstract,        String isRefining,        String isNoDefault    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isRefining = isRefining;
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
    public String getIsnodefault() {
        return isNoDefault;
    }

    public void setIsnodefault(String isNoDefault) {
        this.isNoDefault = isNoDefault;
    }


}