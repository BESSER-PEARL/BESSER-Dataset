





import java.util.List;
import java.util.ArrayList;

public class B1  {






    private List<A1> a1s;


    public B1(
    ) {
        this.a1s = new ArrayList<>();
    }

    public B1(
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