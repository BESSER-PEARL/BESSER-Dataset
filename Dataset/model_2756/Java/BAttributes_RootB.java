





import java.util.List;
import java.util.ArrayList;

public class BAttributes_RootB  {






    private List<BAttributes_B> battributes_bs;




    private BAttributes_B battributes_b;


    public BAttributes_RootB(
    ) {
        this.battributes_bs = new ArrayList<>();
    }

    public BAttributes_RootB(
        ArrayList<BAttributes_B> battributes_bs    ) {
        this.battributes_bs = battributes_bs;
    }


    public List<BAttributes_B> getBattributes_bs() {
        return battributes_bs;
    }

    public void addBattributes_b(Battributes_b battributes_b) {
        this.battributes_bs.add(battributes_b);
    }
    public BAttributes_B getBattributes_b() {
        return battributes_b;
    }

    public void setBattributes_b(BAttributes_B battributes_b) {
        this.battributes_b = battributes_b;
    }

}