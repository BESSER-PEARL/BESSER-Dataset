





import java.util.List;
import java.util.ArrayList;

public class errorkref_C  {






    private List<errorkref_D> errorkref_ds;




    private List<errorkref_L1> errorkref_l1s;




    private List<errorkref_A> errorkref_as;


    public errorkref_C(
    ) {
        this.errorkref_ds = new ArrayList<>();
        this.errorkref_l1s = new ArrayList<>();
        this.errorkref_as = new ArrayList<>();
    }

    public errorkref_C(
        ArrayList<errorkref_D> errorkref_ds,        ArrayList<errorkref_L1> errorkref_l1s,        ArrayList<errorkref_A> errorkref_as    ) {
        this.errorkref_ds = errorkref_ds;
        this.errorkref_l1s = errorkref_l1s;
        this.errorkref_as = errorkref_as;
    }


    public List<errorkref_D> getErrorkref_ds() {
        return errorkref_ds;
    }

    public void addErrorkref_d(Errorkref_d errorkref_d) {
        this.errorkref_ds.add(errorkref_d);
    }
    public List<errorkref_L1> getErrorkref_l1s() {
        return errorkref_l1s;
    }

    public void addErrorkref_l1(Errorkref_l1 errorkref_l1) {
        this.errorkref_l1s.add(errorkref_l1);
    }
    public List<errorkref_A> getErrorkref_as() {
        return errorkref_as;
    }

    public void addErrorkref_a(Errorkref_a errorkref_a) {
        this.errorkref_as.add(errorkref_a);
    }

}