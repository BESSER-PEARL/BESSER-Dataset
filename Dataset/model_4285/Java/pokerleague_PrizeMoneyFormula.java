





import java.util.List;
import java.util.ArrayList;

public class pokerleague_PrizeMoneyFormula extends IdentifiableEntity {

    private int relativePrizeMoney;
    private int rank;



    public pokerleague_PrizeMoneyFormula(
        int relativePrizeMoney,        int rank    ) {
        super(
        );
        this.relativePrizeMoney = relativePrizeMoney;
        this.rank = rank;
    }


    public int getRelativeprizemoney() {
        return relativePrizeMoney;
    }

    public void setRelativeprizemoney(int relativePrizeMoney) {
        this.relativePrizeMoney = relativePrizeMoney;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }


}