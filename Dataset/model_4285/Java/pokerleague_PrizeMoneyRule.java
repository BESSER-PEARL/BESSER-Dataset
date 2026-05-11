





import java.util.List;
import java.util.ArrayList;

public class pokerleague_PrizeMoneyRule extends IdentifiableEntity {

    private int numberOfPlayers;





    private pokerleague_PrizeMoneyFormula pokerleague_prizemoneyformula;




    private List<pokerleague_PrizeMoneyFormula> pokerleague_prizemoneyformulas;


    public pokerleague_PrizeMoneyRule(
        int numberOfPlayers    ) {
        super(
        );
        this.numberOfPlayers = numberOfPlayers;
        this.pokerleague_prizemoneyformulas = new ArrayList<>();
    }

    public pokerleague_PrizeMoneyRule(
        int numberOfPlayers        ArrayList<pokerleague_PrizeMoneyFormula> pokerleague_prizemoneyformulas    ) {
        this.numberOfPlayers = numberOfPlayers;
        this.pokerleague_prizemoneyformulas = pokerleague_prizemoneyformulas;
    }

    public int getNumberofplayers() {
        return numberOfPlayers;
    }

    public void setNumberofplayers(int numberOfPlayers) {
        this.numberOfPlayers = numberOfPlayers;
    }

    public pokerleague_PrizeMoneyFormula getPokerleague_prizemoneyformula() {
        return pokerleague_prizemoneyformula;
    }

    public void setPokerleague_prizemoneyformula(pokerleague_PrizeMoneyFormula pokerleague_prizemoneyformula) {
        this.pokerleague_prizemoneyformula = pokerleague_prizemoneyformula;
    }
    public List<pokerleague_PrizeMoneyFormula> getPokerleague_prizemoneyformulas() {
        return pokerleague_prizemoneyformulas;
    }

    public void addPokerleague_prizemoneyformula(Pokerleague_prizemoneyformula pokerleague_prizemoneyformula) {
        this.pokerleague_prizemoneyformulas.add(pokerleague_prizemoneyformula);
    }

}