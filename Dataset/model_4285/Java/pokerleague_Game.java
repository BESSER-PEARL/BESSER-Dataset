





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Game extends IdentifiableEntity {

    private int ordinal;
    private int buyIn;



    public pokerleague_Game(
        int ordinal,        int buyIn    ) {
        super(
        );
        this.ordinal = ordinal;
        this.buyIn = buyIn;
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


}