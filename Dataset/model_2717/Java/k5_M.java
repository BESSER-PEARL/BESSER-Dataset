





import java.util.List;
import java.util.ArrayList;

public class k5_M  {






    private List<k5_C> k5_cs;


    public k5_M(
    ) {
        this.k5_cs = new ArrayList<>();
    }

    public k5_M(
        ArrayList<k5_C> k5_cs    ) {
        this.k5_cs = k5_cs;
    }


    public List<k5_C> getK5_cs() {
        return k5_cs;
    }

    public void addK5_c(K5_c k5_c) {
        this.k5_cs.add(k5_c);
    }

}