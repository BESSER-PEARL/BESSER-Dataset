





import java.util.List;
import java.util.ArrayList;

public class card_Card  {

    private int rank;
    private boolean flipped;



    public card_Card(
        int rank,        boolean flipped    ) {
        this.rank = rank;
        this.flipped = flipped;
    }


    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public boolean getFlipped() {
        return flipped;
    }

    public void setFlipped(boolean flipped) {
        this.flipped = flipped;
    }


}