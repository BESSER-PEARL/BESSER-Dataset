





import java.util.List;
import java.util.ArrayList;

public class henshin_Rule extends Unit {

    private boolean checkDangling;
    private String javaImports;
    private boolean injectiveMatching;





    private List<henshin_Mapping> henshin_mappings;




    private List<henshin_Mapping> henshin_mappings;




    private henshin_Rule henshin_rule;


    public henshin_Rule(
        boolean checkDangling,        String javaImports,        boolean injectiveMatching    ) {
        super(
        );
        this.checkDangling = checkDangling;
        this.javaImports = javaImports;
        this.injectiveMatching = injectiveMatching;
        this.henshin_mappings = new ArrayList<>();
        this.henshin_mappings = new ArrayList<>();
    }

    public henshin_Rule(
        boolean checkDangling,        String javaImports,        boolean injectiveMatching        ArrayList<henshin_Mapping> henshin_mappings,        ArrayList<henshin_Mapping> henshin_mappings    ) {
        this.checkDangling = checkDangling;
        this.javaImports = javaImports;
        this.injectiveMatching = injectiveMatching;
        this.henshin_mappings = henshin_mappings;
        this.henshin_mappings = henshin_mappings;
    }

    public boolean getCheckdangling() {
        return checkDangling;
    }

    public void setCheckdangling(boolean checkDangling) {
        this.checkDangling = checkDangling;
    }
    public String getJavaimports() {
        return javaImports;
    }

    public void setJavaimports(String javaImports) {
        this.javaImports = javaImports;
    }
    public boolean getInjectivematching() {
        return injectiveMatching;
    }

    public void setInjectivematching(boolean injectiveMatching) {
        this.injectiveMatching = injectiveMatching;
    }

    public List<henshin_Mapping> getHenshin_mappings() {
        return henshin_mappings;
    }

    public void addHenshin_mapping(Henshin_mapping henshin_mapping) {
        this.henshin_mappings.add(henshin_mapping);
    }
    public List<henshin_Mapping> getHenshin_mappings() {
        return henshin_mappings;
    }

    public void addHenshin_mapping(Henshin_mapping henshin_mapping) {
        this.henshin_mappings.add(henshin_mapping);
    }
    public henshin_Rule getHenshin_rule() {
        return henshin_rule;
    }

    public void setHenshin_rule(henshin_Rule henshin_rule) {
        this.henshin_rule = henshin_rule;
    }

}