





import java.util.List;
import java.util.ArrayList;

public class refac_X  {






    private List<refac_A> refac_as;




    private List<refac_K> refac_ks;


    public refac_X(
    ) {
        this.refac_as = new ArrayList<>();
        this.refac_ks = new ArrayList<>();
    }

    public refac_X(
        ArrayList<refac_A> refac_as,        ArrayList<refac_K> refac_ks    ) {
        this.refac_as = refac_as;
        this.refac_ks = refac_ks;
    }


    public List<refac_A> getRefac_as() {
        return refac_as;
    }

    public void addRefac_a(Refac_a refac_a) {
        this.refac_as.add(refac_a);
    }
    public List<refac_K> getRefac_ks() {
        return refac_ks;
    }

    public void addRefac_k(Refac_k refac_k) {
        this.refac_ks.add(refac_k);
    }

}