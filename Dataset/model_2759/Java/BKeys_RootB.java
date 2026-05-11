





import java.util.List;
import java.util.ArrayList;

public class BKeys_RootB  {






    private List<BKeys_B> bkeys_bs;




    private BKeys_B bkeys_b;


    public BKeys_RootB(
    ) {
        this.bkeys_bs = new ArrayList<>();
    }

    public BKeys_RootB(
        ArrayList<BKeys_B> bkeys_bs    ) {
        this.bkeys_bs = bkeys_bs;
    }


    public List<BKeys_B> getBkeys_bs() {
        return bkeys_bs;
    }

    public void addBkeys_b(Bkeys_b bkeys_b) {
        this.bkeys_bs.add(bkeys_b);
    }
    public BKeys_B getBkeys_b() {
        return bkeys_b;
    }

    public void setBkeys_b(BKeys_B bkeys_b) {
        this.bkeys_b = bkeys_b;
    }

}