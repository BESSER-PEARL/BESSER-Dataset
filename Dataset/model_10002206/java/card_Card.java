





import java.util.List;
import java.util.ArrayList;

public class card_Card  {

    private boolean flipped;
    private int rank;



    public card_Card(
        boolean flipped,        int rank    ) {
        this.flipped = flipped;
        this.rank = rank;
    }


    public boolean getFlipped() {
        return flipped;
    }

    public void setFlipped(boolean flipped) {
        this.flipped = flipped;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }


}