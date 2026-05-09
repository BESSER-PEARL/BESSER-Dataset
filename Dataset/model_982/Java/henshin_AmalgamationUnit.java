





import java.util.List;
import java.util.ArrayList;

public class henshin_AmalgamationUnit extends TransformationUnit {






    private henshin_Rule henshin_rule;




    private List<henshin_Rule> henshin_rules;


    public henshin_AmalgamationUnit(
    ) {
        super(
        );
        this.henshin_rules = new ArrayList<>();
    }

    public henshin_AmalgamationUnit(
        ArrayList<henshin_Rule> henshin_rules    ) {
        this.henshin_rules = henshin_rules;
    }


    public henshin_Rule getHenshin_rule() {
        return henshin_rule;
    }

    public void setHenshin_rule(henshin_Rule henshin_rule) {
        this.henshin_rule = henshin_rule;
    }
    public List<henshin_Rule> getHenshin_rules() {
        return henshin_rules;
    }

    public void addHenshin_rule(Henshin_rule henshin_rule) {
        this.henshin_rules.add(henshin_rule);
    }

}