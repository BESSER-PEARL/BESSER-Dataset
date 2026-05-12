





import java.util.List;
import java.util.ArrayList;

public class R  {






    private List<A1> a1s;


    public R(
    ) {
        this.a1s = new ArrayList<>();
    }

    public R(
        ArrayList<A1> a1s    ) {
        this.a1s = a1s;
    }


    public List<A1> getA1s() {
        return a1s;
    }

    public void addA1(A1 a1) {
        this.a1s.add(a1);
    }

}