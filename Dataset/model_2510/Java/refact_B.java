





import java.util.List;
import java.util.ArrayList;

public class refact_B extends Named {






    private refact_C refact_c;




    private refact_C refact_c;




    private List<refact_C> refact_cs;




    private List<refact_D> refact_ds;


    public refact_B(
    ) {
        super(
        );
        this.refact_cs = new ArrayList<>();
        this.refact_ds = new ArrayList<>();
    }

    public refact_B(
        ArrayList<refact_C> refact_cs,        ArrayList<refact_D> refact_ds    ) {
        this.refact_cs = refact_cs;
        this.refact_ds = refact_ds;
    }


    public refact_C getRefact_c() {
        return refact_c;
    }

    public void setRefact_c(refact_C refact_c) {
        this.refact_c = refact_c;
    }
    public refact_C getRefact_c() {
        return refact_c;
    }

    public void setRefact_c(refact_C refact_c) {
        this.refact_c = refact_c;
    }
    public List<refact_C> getRefact_cs() {
        return refact_cs;
    }

    public void addRefact_c(Refact_c refact_c) {
        this.refact_cs.add(refact_c);
    }
    public List<refact_D> getRefact_ds() {
        return refact_ds;
    }

    public void addRefact_d(Refact_d refact_d) {
        this.refact_ds.add(refact_d);
    }

}