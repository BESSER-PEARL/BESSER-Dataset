





import java.util.List;
import java.util.ArrayList;

public class cycle_A  {

    private int i;





    private List<cycle_B> cycle_bs;




    private cycle_B cycle_b;




    private cycle_C cycle_c;


    public cycle_A(
        int i    ) {
        this.i = i;
        this.cycle_bs = new ArrayList<>();
    }

    public cycle_A(
        int i        ArrayList<cycle_B> cycle_bs    ) {
        this.i = i;
        this.cycle_bs = cycle_bs;
    }

    public int getI() {
        return i;
    }

    public void setI(int i) {
        this.i = i;
    }

    public List<cycle_B> getCycle_bs() {
        return cycle_bs;
    }

    public void addCycle_b(Cycle_b cycle_b) {
        this.cycle_bs.add(cycle_b);
    }
    public cycle_B getCycle_b() {
        return cycle_b;
    }

    public void setCycle_b(cycle_B cycle_b) {
        this.cycle_b = cycle_b;
    }
    public cycle_C getCycle_c() {
        return cycle_c;
    }

    public void setCycle_c(cycle_C cycle_c) {
        this.cycle_c = cycle_c;
    }

}