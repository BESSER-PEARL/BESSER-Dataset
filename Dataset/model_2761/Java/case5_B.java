





import java.util.List;
import java.util.ArrayList;

public class case5_B  {






    private List<case5_D> case5_ds;




    private case5_N case5_n;


    public case5_B(
    ) {
        this.case5_ds = new ArrayList<>();
    }

    public case5_B(
        ArrayList<case5_D> case5_ds    ) {
        this.case5_ds = case5_ds;
    }


    public List<case5_D> getCase5_ds() {
        return case5_ds;
    }

    public void addCase5_d(Case5_d case5_d) {
        this.case5_ds.add(case5_d);
    }
    public case5_N getCase5_n() {
        return case5_n;
    }

    public void setCase5_n(case5_N case5_n) {
        this.case5_n = case5_n;
    }

}