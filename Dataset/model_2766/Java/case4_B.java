





import java.util.List;
import java.util.ArrayList;

public class case4_B extends Named {






    private List<case4_D> case4_ds;




    private case4_N case4_n;


    public case4_B(
    ) {
        super(
        );
        this.case4_ds = new ArrayList<>();
    }

    public case4_B(
        ArrayList<case4_D> case4_ds    ) {
        this.case4_ds = case4_ds;
    }


    public List<case4_D> getCase4_ds() {
        return case4_ds;
    }

    public void addCase4_d(Case4_d case4_d) {
        this.case4_ds.add(case4_d);
    }
    public case4_N getCase4_n() {
        return case4_n;
    }

    public void setCase4_n(case4_N case4_n) {
        this.case4_n = case4_n;
    }

}