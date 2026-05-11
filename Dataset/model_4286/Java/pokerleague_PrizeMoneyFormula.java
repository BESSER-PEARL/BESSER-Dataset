





import java.util.List;
import java.util.ArrayList;

public class pokerleague_PrizeMoneyFormula extends IdentifiableEntity {

    private int rank;
    private int relativePrizeMoney;



    public pokerleague_PrizeMoneyFormula(
        int rank,        int relativePrizeMoney    ) {
        super(
        );
        this.rank = rank;
        this.relativePrizeMoney = relativePrizeMoney;
    }


    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public int getRelativeprizemoney() {
        return relativePrizeMoney;
    }

    public void setRelativeprizemoney(int relativePrizeMoney) {
        this.relativePrizeMoney = relativePrizeMoney;
    }


}