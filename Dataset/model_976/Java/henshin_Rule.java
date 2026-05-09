





import java.util.List;
import java.util.ArrayList;

public class henshin_Rule extends Unit {

    private boolean checkDangling;
    private boolean injectiveMatching;
    private String javaImports;





    private List<henshin_Rule> henshin_rules;


    public henshin_Rule(
        boolean checkDangling,        boolean injectiveMatching,        String javaImports    ) {
        super(
        );
        this.checkDangling = checkDangling;
        this.injectiveMatching = injectiveMatching;
        this.javaImports = javaImports;
        this.henshin_rules = new ArrayList<>();
    }

    public henshin_Rule(
        boolean checkDangling,        boolean injectiveMatching,        String javaImports        ArrayList<henshin_Rule> henshin_rules    ) {
        this.checkDangling = checkDangling;
        this.injectiveMatching = injectiveMatching;
        this.javaImports = javaImports;
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
    public String getJavaimports() {
        return javaImports;
    }

    public void setJavaimports(String javaImports) {
        this.javaImports = javaImports;
    }

    public List<henshin_Rule> getHenshin_rules() {
        return henshin_rules;
    }

    public void addHenshin_rule(Henshin_rule henshin_rule) {
        this.henshin_rules.add(henshin_rule);
    }

}