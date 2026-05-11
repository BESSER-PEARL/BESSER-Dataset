





import java.util.List;
import java.util.ArrayList;

public class k7_M  {






    private List<k7_C> k7_cs;


    public k7_M(
    ) {
        this.k7_cs = new ArrayList<>();
    }

    public k7_M(
        ArrayList<k7_C> k7_cs    ) {
        this.k7_cs = k7_cs;
    }


    public List<k7_C> getK7_cs() {
        return k7_cs;
    }

    public void addK7_c(K7_c k7_c) {
        this.k7_cs.add(k7_c);
    }

}