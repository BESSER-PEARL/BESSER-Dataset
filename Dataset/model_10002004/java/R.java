





import java.util.List;
import java.util.ArrayList;

public class R  {






    private List<X> xs;


    public R(
    ) {
        this.xs = new ArrayList<>();
    }

    public R(
        ArrayList<X> xs    ) {
        this.xs = xs;
    }


    public List<X> getXs() {
        return xs;
    }

    public void addX(X x) {
        this.xs.add(x);
    }

}