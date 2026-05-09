





import java.util.List;
import java.util.ArrayList;

public class henshin_Rule extends Unit {

    private boolean checkDangling;
    private boolean injectiveMatching;
    private String injectiveMatchingPresenceCondition;
    private String featureModel;





    private List<henshin_Rule> henshin_rules;


    public henshin_Rule(
        boolean checkDangling,        boolean injectiveMatching,        String injectiveMatchingPresenceCondition,        String featureModel    ) {
        super(
        );
        this.checkDangling = checkDangling;
        this.injectiveMatching = injectiveMatching;
        this.injectiveMatchingPresenceCondition = injectiveMatchingPresenceCondition;
        this.featureModel = featureModel;
        this.henshin_rules = new ArrayList<>();
    }

    public henshin_Rule(
        boolean checkDangling,        boolean injectiveMatching,        String injectiveMatchingPresenceCondition,        String featureModel        ArrayList<henshin_Rule> henshin_rules    ) {
        this.checkDangling = checkDangling;
        this.injectiveMatching = injectiveMatching;
        this.injectiveMatchingPresenceCondition = injectiveMatchingPresenceCondition;
        this.featureModel = featureModel;
        this.henshin_rules = henshin_rules;
    }

    public boolean getCheckdangling() {
        return checkDangling;
    }

    public void setCheckdangling(boolean checkDangling) {
        this.checkDangling = checkDangling;
    }
    public boolean getInjectivematching() {
        return injectiveMatching;
    }

    public void setInjectivematching(boolean injectiveMatching) {
        this.injectiveMatching = injectiveMatching;
    }
    public String getInjectivematchingpresencecondition() {
        return injectiveMatchingPresenceCondition;
    }

    public void setInjectivematchingpresencecondition(String injectiveMatchingPresenceCondition) {
        this.injectiveMatchingPresenceCondition = injectiveMatchingPresenceCondition;
    }
    public String getFeaturemodel() {
        return featureModel;
    }

    public void setFeaturemodel(String featureModel) {
        this.featureModel = featureModel;
    }

    public List<henshin_Rule> getHenshin_rules() {
        return henshin_rules;
    }

    public void addHenshin_rule(Henshin_rule henshin_rule) {
        this.henshin_rules.add(henshin_rule);
    }

}