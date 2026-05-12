





import java.util.List;
import java.util.ArrayList;

public class R  {






    private List<A> as;


    public R(
    ) {
        this.as = new ArrayList<>();
    }

    public R(
        ArrayList<A> as    ) {
        this.as = as;
    }


    public List<A> getAs() {
        return as;
    }

    public void addA(A a) {
        this.as.add(a);
    }

}