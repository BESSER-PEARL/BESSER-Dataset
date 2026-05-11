





import java.util.List;
import java.util.ArrayList;

public class pokerleague_PrizeMoneyRuleSet extends DescribedEntity {






    private pokerleague_Game pokerleague_game;




    private List<pokerleague_PrizeMoneyRule> pokerleague_prizemoneyrules;




    private pokerleague_PrizeMoneyRule pokerleague_prizemoneyrule;


    public pokerleague_PrizeMoneyRuleSet(
    ) {
        super(
        );
        this.pokerleague_prizemoneyrules = new ArrayList<>();
    }

    public pokerleague_PrizeMoneyRuleSet(
        ArrayList<pokerleague_PrizeMoneyRule> pokerleague_prizemoneyrules    ) {
        this.pokerleague_prizemoneyrules = pokerleague_prizemoneyrules;
    }


    public pokerleague_Game getPokerleague_game() {
        return pokerleague_game;
    }

    public void setPokerleague_game(pokerleague_Game pokerleague_game) {
        this.pokerleague_game = pokerleague_game;
    }
    public List<pokerleague_PrizeMoneyRule> getPokerleague_prizemoneyrules() {
        return pokerleague_prizemoneyrules;
    }

    public void addPokerleague_prizemoneyrule(Pokerleague_prizemoneyrule pokerleague_prizemoneyrule) {
        this.pokerleague_prizemoneyrules.add(pokerleague_prizemoneyrule);
    }
    public pokerleague_PrizeMoneyRule getPokerleague_prizemoneyrule() {
        return pokerleague_prizemoneyrule;
    }

    public void setPokerleague_prizemoneyrule(pokerleague_PrizeMoneyRule pokerleague_prizemoneyrule) {
        this.pokerleague_prizemoneyrule = pokerleague_prizemoneyrule;
    }

}