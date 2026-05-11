





import java.util.List;
import java.util.ArrayList;

public class pokerleague_PrizeMoneyRule extends IdentifiableEntity {

    private int numberOfPlayers;



    public pokerleague_PrizeMoneyRule(
        int numberOfPlayers    ) {
        super(
        );
        this.numberOfPlayers = numberOfPlayers;
    }


    public int getNumberofplayers() {
        return numberOfPlayers;
    }

    public void setNumberofplayers(int numberOfPlayers) {
        this.numberOfPlayers = numberOfPlayers;
    }


}