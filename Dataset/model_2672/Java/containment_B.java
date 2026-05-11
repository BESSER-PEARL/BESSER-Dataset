





import java.util.List;
import java.util.ArrayList;

public class containment_B extends Named {






    private containment_A containment_a;




    private List<containment_C> containment_cs;




    private List<containment_G> containment_gs;


    public containment_B(
    ) {
        super(
        );
        this.containment_cs = new ArrayList<>();
        this.containment_gs = new ArrayList<>();
    }

    public containment_B(
        ArrayList<containment_C> containment_cs,        ArrayList<containment_G> containment_gs    ) {
        this.containment_cs = containment_cs;
        this.containment_gs = containment_gs;
    }


    public containment_A getContainment_a() {
        return containment_a;
    }

    public void setContainment_a(containment_A containment_a) {
        this.containment_a = containment_a;
    }
    public List<containment_C> getContainment_cs() {
        return containment_cs;
    }

    public void addContainment_c(Containment_c containment_c) {
        this.containment_cs.add(containment_c);
    }
    public List<containment_G> getContainment_gs() {
        return containment_gs;
    }

    public void addContainment_g(Containment_g containment_g) {
        this.containment_gs.add(containment_g);
    }

}