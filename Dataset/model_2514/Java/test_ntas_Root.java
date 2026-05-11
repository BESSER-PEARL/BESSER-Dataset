





import java.util.List;
import java.util.ArrayList;

public class test_ntas_Root  {






    private List<D> ds;




    private C c;


    public test_ntas_Root(
    ) {
        this.ds = new ArrayList<>();
    }

    public test_ntas_Root(
        ArrayList<D> ds    ) {
        this.ds = ds;
    }


    public List<D> getDs() {
        return ds;
    }

    public void addD(D d) {
        this.ds.add(d);
    }
    public C getC() {
        return c;
    }

    public void setC(C c) {
        this.c = c;
    }

}