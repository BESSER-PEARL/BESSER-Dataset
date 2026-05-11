





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Game extends IdentifiableEntity {

    private int buyIn;
    private int ordinal;



    public pokerleague_Game(
        int buyIn,        int ordinal    ) {
        super(
        );
        this.buyIn = buyIn;
        this.ordinal = ordinal;
    }


    public int getBuyin() {
        return buyIn;
    }

    public void setBuyin(int buyIn) {
        this.buyIn = buyIn;
    }
    public int getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(int ordinal) {
        this.ordinal = ordinal;
    }


}