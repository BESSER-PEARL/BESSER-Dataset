





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_RuleWithPattern extends Rule {

    private String isRefining;
    private String isAbstract;
    private String isNoDefault;





    private RuleWithPattern rulewithpattern;




    private List<RuleWithPattern> rulewithpatterns;


    public atlext_ATL_RuleWithPattern(
        String isRefining,        String isAbstract,        String isNoDefault    ) {
        super(
        );
        this.isRefining = isRefining;
        this.isAbstract = isAbstract;
        this.isNoDefault = isNoDefault;
        this.rulewithpatterns = new ArrayList<>();
    }

    public atlext_ATL_RuleWithPattern(
        String isRefining,        String isAbstract,        String isNoDefault        ArrayList<RuleWithPattern> rulewithpatterns    ) {
        this.isRefining = isRefining;
        this.isAbstract = isAbstract;
        this.isNoDefault = isNoDefault;
        this.rulewithpatterns = rulewithpatterns;
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
    public String getIsnodefault() {
        return isNoDefault;
    }

    public void setIsnodefault(String isNoDefault) {
        this.isNoDefault = isNoDefault;
    }

    public RuleWithPattern getRulewithpattern() {
        return rulewithpattern;
    }

    public void setRulewithpattern(RuleWithPattern rulewithpattern) {
        this.rulewithpattern = rulewithpattern;
    }
    public List<RuleWithPattern> getRulewithpatterns() {
        return rulewithpatterns;
    }

    public void addRulewithpattern(Rulewithpattern rulewithpattern) {
        this.rulewithpatterns.add(rulewithpattern);
    }

}