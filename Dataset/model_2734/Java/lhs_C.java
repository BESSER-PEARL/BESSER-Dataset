





import java.util.List;
import java.util.ArrayList;

public class lhs_C  {

    private String c;





    private lhs_A lhs_a;




    private List<lhs_B> lhs_bs;


    public lhs_C(
        String c    ) {
        this.c = c;
        this.lhs_bs = new ArrayList<>();
    }

    public lhs_C(
        String c        ArrayList<lhs_B> lhs_bs    ) {
        this.c = c;
        this.lhs_bs = lhs_bs;
    }

    public String getC() {
        return c;
    }

    public void setC(String c) {
        this.c = c;
    }

    public lhs_A getLhs_a() {
        return lhs_a;
    }

    public void setLhs_a(lhs_A lhs_a) {
        this.lhs_a = lhs_a;
    }
    public List<lhs_B> getLhs_bs() {
        return lhs_bs;
    }

    public void addLhs_b(Lhs_b lhs_b) {
        this.lhs_bs.add(lhs_b);
    }

}