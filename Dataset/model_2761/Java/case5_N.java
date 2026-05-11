





import java.util.List;
import java.util.ArrayList;

public class case5_N  {






    private List<case5_A> case5_as;




    private List<case5_T> case5_ts;


    public case5_N(
    ) {
        this.case5_as = new ArrayList<>();
        this.case5_ts = new ArrayList<>();
    }

    public case5_N(
        ArrayList<case5_A> case5_as,        ArrayList<case5_T> case5_ts    ) {
        this.case5_as = case5_as;
        this.case5_ts = case5_ts;
    }


    public List<case5_A> getCase5_as() {
        return case5_as;
    }

    public void addCase5_a(Case5_a case5_a) {
        this.case5_as.add(case5_a);
    }
    public List<case5_T> getCase5_ts() {
        return case5_ts;
    }

    public void addCase5_t(Case5_t case5_t) {
        this.case5_ts.add(case5_t);
    }

}