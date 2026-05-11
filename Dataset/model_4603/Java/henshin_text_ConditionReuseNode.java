





import java.util.List;
import java.util.ArrayList;

public class henshin_text_ConditionReuseNode extends ConditionGraphElements {






    private List<henshin_text_Match> henshin_text_matchs;




    private henshin_text_ConditionNodeTypes henshin_text_conditionnodetypes;


    public henshin_text_ConditionReuseNode(
    ) {
        super(
        );
        this.henshin_text_matchs = new ArrayList<>();
    }

    public henshin_text_ConditionReuseNode(
        ArrayList<henshin_text_Match> henshin_text_matchs    ) {
        this.henshin_text_matchs = henshin_text_matchs;
    }


    public List<henshin_text_Match> getHenshin_text_matchs() {
        return henshin_text_matchs;
    }

    public void addHenshin_text_match(Henshin_text_match henshin_text_match) {
        this.henshin_text_matchs.add(henshin_text_match);
    }
    public henshin_text_ConditionNodeTypes getHenshin_text_conditionnodetypes() {
        return henshin_text_conditionnodetypes;
    }

    public void setHenshin_text_conditionnodetypes(henshin_text_ConditionNodeTypes henshin_text_conditionnodetypes) {
        this.henshin_text_conditionnodetypes = henshin_text_conditionnodetypes;
    }

}