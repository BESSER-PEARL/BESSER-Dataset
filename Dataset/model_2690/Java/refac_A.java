





import java.util.List;
import java.util.ArrayList;

public class refac_A  {






    private List<refac_B> refac_bs;


    public refac_A(
    ) {
        this.refac_bs = new ArrayList<>();
    }

    public refac_A(
        ArrayList<refac_B> refac_bs    ) {
        this.refac_bs = refac_bs;
    }


    public List<refac_B> getRefac_bs() {
        return refac_bs;
    }

    public void addRefac_b(Refac_b refac_b) {
        this.refac_bs.add(refac_b);
    }

}