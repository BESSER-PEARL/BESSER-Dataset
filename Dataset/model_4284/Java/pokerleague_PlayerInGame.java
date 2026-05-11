





import java.util.List;
import java.util.ArrayList;

public class pokerleague_PlayerInGame extends IdentifiableEntity {

    private int rank;





    private pokerleague_Player pokerleague_player;


    public pokerleague_PlayerInGame(
        int rank    ) {
        super(
        );
        this.rank = rank;
    }


    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }

    public pokerleague_Player getPokerleague_player() {
        return pokerleague_player;
    }

    public void setPokerleague_player(pokerleague_Player pokerleague_player) {
        this.pokerleague_player = pokerleague_player;
    }

}