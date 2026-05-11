





import java.util.List;
import java.util.ArrayList;

public class k5_X  {






    private List<k5_P> k5_ps;


    public k5_X(
    ) {
        this.k5_ps = new ArrayList<>();
    }

    public k5_X(
        ArrayList<k5_P> k5_ps    ) {
        this.k5_ps = k5_ps;
    }


    public List<k5_P> getK5_ps() {
        return k5_ps;
    }

    public void addK5_p(K5_p k5_p) {
        this.k5_ps.add(k5_p);
    }

}