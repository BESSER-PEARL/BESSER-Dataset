





import java.util.List;
import java.util.ArrayList;

public class k5_P  {






    private List<k5_J> k5_js;


    public k5_P(
    ) {
        this.k5_js = new ArrayList<>();
    }

    public k5_P(
        ArrayList<k5_J> k5_js    ) {
        this.k5_js = k5_js;
    }


    public List<k5_J> getK5_js() {
        return k5_js;
    }

    public void addK5_j(K5_j k5_j) {
        this.k5_js.add(k5_j);
    }

}