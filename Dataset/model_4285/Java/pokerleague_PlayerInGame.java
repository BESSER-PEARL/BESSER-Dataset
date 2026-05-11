





import java.util.List;
import java.util.ArrayList;

public class pokerleague_PlayerInGame extends IdentifiableEntity {

    private int rank;





    private pokerleague_Game pokerleague_game;




    private pokerleague_Player pokerleague_player;




    private pokerleague_Game pokerleague_game;


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

    public pokerleague_Game getPokerleague_game() {
        return pokerleague_game;
    }

    public void setPokerleague_game(pokerleague_Game pokerleague_game) {
        this.pokerleague_game = pokerleague_game;
    }
    public pokerleague_Player getPokerleague_player() {
        return pokerleague_player;
    }

    public void setPokerleague_player(pokerleague_Player pokerleague_player) {
        this.pokerleague_player = pokerleague_player;
    }
    public pokerleague_Game getPokerleague_game() {
        return pokerleague_game;
    }

    public void setPokerleague_game(pokerleague_Game pokerleague_game) {
        this.pokerleague_game = pokerleague_game;
    }

}