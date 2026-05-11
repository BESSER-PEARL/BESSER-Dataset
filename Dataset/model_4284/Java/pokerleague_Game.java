





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Game extends IdentifiableEntity {

    private int ordinal;
    private int buyIn;





    private pokerleague_PlayerInGame pokerleague_playeringame;




    private List<pokerleague_PlayerInGame> pokerleague_playeringames;


    public pokerleague_Game(
        int ordinal,        int buyIn    ) {
        super(
        );
        this.ordinal = ordinal;
        this.buyIn = buyIn;
        this.pokerleague_playeringames = new ArrayList<>();
    }

    public pokerleague_Game(
        int ordinal,        int buyIn        ArrayList<pokerleague_PlayerInGame> pokerleague_playeringames    ) {
        this.ordinal = ordinal;
        this.buyIn = buyIn;
        this.pokerleague_playeringames = pokerleague_playeringames;
    }

    public int getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(int ordinal) {
        this.ordinal = ordinal;
    }
    public int getBuyin() {
        return buyIn;
    }

    public void setBuyin(int buyIn) {
        this.buyIn = buyIn;
    }

    public pokerleague_PlayerInGame getPokerleague_playeringame() {
        return pokerleague_playeringame;
    }

    public void setPokerleague_playeringame(pokerleague_PlayerInGame pokerleague_playeringame) {
        this.pokerleague_playeringame = pokerleague_playeringame;
    }
    public List<pokerleague_PlayerInGame> getPokerleague_playeringames() {
        return pokerleague_playeringames;
    }

    public void addPokerleague_playeringame(Pokerleague_playeringame pokerleague_playeringame) {
        this.pokerleague_playeringames.add(pokerleague_playeringame);
    }

}