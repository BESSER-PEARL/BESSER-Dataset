





import java.util.List;
import java.util.ArrayList;

public class k2_M  {






    private List<k2_C> k2_cs;


    public k2_M(
    ) {
        this.k2_cs = new ArrayList<>();
    }

    public k2_M(
        ArrayList<k2_C> k2_cs    ) {
        this.k2_cs = k2_cs;
    }


    public List<k2_C> getK2_cs() {
        return k2_cs;
    }

    public void addK2_c(K2_c k2_c) {
        this.k2_cs.add(k2_c);
    }

}