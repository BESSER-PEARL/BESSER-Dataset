





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Rule extends ModelElement {






    private List<henshin_text_RuleElement> henshin_text_ruleelements;


    public henshin_text_Rule(
    ) {
        super(
        );
        this.henshin_text_ruleelements = new ArrayList<>();
    }

    public henshin_text_Rule(
        ArrayList<henshin_text_RuleElement> henshin_text_ruleelements    ) {
        this.henshin_text_ruleelements = henshin_text_ruleelements;
    }


    public List<henshin_text_RuleElement> getHenshin_text_ruleelements() {
        return henshin_text_ruleelements;
    }

    public void addHenshin_text_ruleelement(Henshin_text_ruleelement henshin_text_ruleelement) {
        this.henshin_text_ruleelements.add(henshin_text_ruleelement);
    }

}