





import java.util.List;
import java.util.ArrayList;

public class ATL_MatchedRule extends Rule {

    private String isAbstract;
    private String isRefining;
    private String isNoDefault;





    private MatchedRule matchedrule;




    private List<MatchedRule> matchedrules;


    public ATL_MatchedRule(
        String isAbstract,        String isRefining,        String isNoDefault    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isRefining = isRefining;
        this.isNoDefault = isNoDefault;
        this.matchedrules = new ArrayList<>();
    }

    public ATL_MatchedRule(
        String isAbstract,        String isRefining,        String isNoDefault        ArrayList<MatchedRule> matchedrules    ) {
        this.isAbstract = isAbstract;
        this.isRefining = isRefining;
        this.isNoDefault = isNoDefault;
        this.matchedrules = matchedrules;
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

    public MatchedRule getMatchedrule() {
        return matchedrule;
    }

    public void setMatchedrule(MatchedRule matchedrule) {
        this.matchedrule = matchedrule;
    }
    public List<MatchedRule> getMatchedrules() {
        return matchedrules;
    }

    public void addMatchedrule(Matchedrule matchedrule) {
        this.matchedrules.add(matchedrule);
    }

}