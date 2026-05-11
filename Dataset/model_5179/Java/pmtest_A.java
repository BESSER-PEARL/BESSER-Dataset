





import java.util.List;
import java.util.ArrayList;

public class pmtest_A  {

    private int i;





    private pmtest_A pmtest_a;




    private List<pmtest_D> pmtest_ds;




    private pmtest_A pmtest_a;


    public pmtest_A(
        int i    ) {
        this.i = i;
        this.pmtest_ds = new ArrayList<>();
    }

    public pmtest_A(
        int i        ArrayList<pmtest_D> pmtest_ds    ) {
        this.i = i;
        this.pmtest_ds = pmtest_ds;
    }

    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
    }

    public pmtest_A getPmtest_a() {
        return pmtest_a;
    }

    public void setPmtest_a(pmtest_A pmtest_a) {
        this.pmtest_a = pmtest_a;
    }
    public List<pmtest_D> getPmtest_ds() {
        return pmtest_ds;
    }

    public void addPmtest_d(Pmtest_d pmtest_d) {
        this.pmtest_ds.add(pmtest_d);
    }
    public pmtest_A getPmtest_a() {
        return pmtest_a;
    }

    public void setPmtest_a(pmtest_A pmtest_a) {
        this.pmtest_a = pmtest_a;
    }

}