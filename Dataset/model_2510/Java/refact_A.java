





import java.util.List;
import java.util.ArrayList;

public class refact_A  {






    private List<refact_B> refact_bs;




    private List<refact_E> refact_es;


    public refact_A(
    ) {
        this.refact_bs = new ArrayList<>();
        this.refact_es = new ArrayList<>();
    }

    public refact_A(
        ArrayList<refact_B> refact_bs,        ArrayList<refact_E> refact_es    ) {
        this.refact_bs = refact_bs;
        this.refact_es = refact_es;
    }


    public List<refact_B> getRefact_bs() {
        return refact_bs;
    }

    public void addRefact_b(Refact_b refact_b) {
        this.refact_bs.add(refact_b);
    }
    public List<refact_E> getRefact_es() {
        return refact_es;
    }

    public void addRefact_e(Refact_e refact_e) {
        this.refact_es.add(refact_e);
    }

}