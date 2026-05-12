





import java.util.List;
import java.util.ArrayList;

public class R2  {






    private List<A12> a12s;


    public R2(
    ) {
        this.a12s = new ArrayList<>();
    }

    public R2(
        ArrayList<A12> a12s    ) {
        this.a12s = a12s;
    }


    public List<A12> getA12s() {
        return a12s;
    }

    public void addA12(A12 a12) {
        this.a12s.add(a12);
    }

}