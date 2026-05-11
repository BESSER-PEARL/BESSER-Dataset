





import java.util.List;
import java.util.ArrayList;

public class refac_C  {






    private refac_A refac_a;




    private List<refac_B> refac_bs;


    public refac_C(
    ) {
        this.refac_bs = new ArrayList<>();
    }

    public refac_C(
        ArrayList<refac_B> refac_bs    ) {
        this.refac_bs = refac_bs;
    }


    public refac_A getRefac_a() {
        return refac_a;
    }

    public void setRefac_a(refac_A refac_a) {
        this.refac_a = refac_a;
    }
    public List<refac_B> getRefac_bs() {
        return refac_bs;
    }

    public void addRefac_b(Refac_b refac_b) {
        this.refac_bs.add(refac_b);
    }

}