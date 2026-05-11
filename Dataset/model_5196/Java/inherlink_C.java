





import java.util.List;
import java.util.ArrayList;

public class inherlink_C  {






    private List<inherlink_M> inherlink_ms;




    private List<inherlink_K> inherlink_ks;




    private List<inherlink_X> inherlink_xs;




    private List<inherlink_N> inherlink_ns;


    public inherlink_C(
    ) {
        this.inherlink_ms = new ArrayList<>();
        this.inherlink_ks = new ArrayList<>();
        this.inherlink_xs = new ArrayList<>();
        this.inherlink_ns = new ArrayList<>();
    }

    public inherlink_C(
        ArrayList<inherlink_M> inherlink_ms,        ArrayList<inherlink_K> inherlink_ks,        ArrayList<inherlink_X> inherlink_xs,        ArrayList<inherlink_N> inherlink_ns    ) {
        this.inherlink_ms = inherlink_ms;
        this.inherlink_ks = inherlink_ks;
        this.inherlink_xs = inherlink_xs;
        this.inherlink_ns = inherlink_ns;
    }


    public List<inherlink_M> getInherlink_ms() {
        return inherlink_ms;
    }

    public void addInherlink_m(Inherlink_m inherlink_m) {
        this.inherlink_ms.add(inherlink_m);
    }
    public List<inherlink_K> getInherlink_ks() {
        return inherlink_ks;
    }

    public void addInherlink_k(Inherlink_k inherlink_k) {
        this.inherlink_ks.add(inherlink_k);
    }
    public List<inherlink_X> getInherlink_xs() {
        return inherlink_xs;
    }

    public void addInherlink_x(Inherlink_x inherlink_x) {
        this.inherlink_xs.add(inherlink_x);
    }
    public List<inherlink_N> getInherlink_ns() {
        return inherlink_ns;
    }

    public void addInherlink_n(Inherlink_n inherlink_n) {
        this.inherlink_ns.add(inherlink_n);
    }

}