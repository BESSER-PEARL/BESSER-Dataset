





import java.util.List;
import java.util.ArrayList;

public class BBase_RootB  {






    private BBase_B bbase_b;




    private List<BBase_B> bbase_bs;


    public BBase_RootB(
    ) {
        this.bbase_bs = new ArrayList<>();
    }

    public BBase_RootB(
        ArrayList<BBase_B> bbase_bs    ) {
        this.bbase_bs = bbase_bs;
    }


    public BBase_B getBbase_b() {
        return bbase_b;
    }

    public void setBbase_b(BBase_B bbase_b) {
        this.bbase_b = bbase_b;
    }
    public List<BBase_B> getBbase_bs() {
        return bbase_bs;
    }

    public void addBbase_b(Bbase_b bbase_b) {
        this.bbase_bs.add(bbase_b);
    }

}