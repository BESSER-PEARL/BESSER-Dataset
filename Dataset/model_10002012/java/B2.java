





import java.util.List;
import java.util.ArrayList;

public class B2  {






    private List<A2> a2s;


    public B2(
    ) {
        this.a2s = new ArrayList<>();
    }

    public B2(
        ArrayList<A2> a2s    ) {
        this.a2s = a2s;
    }


    public List<A2> getA2s() {
        return a2s;
    }

    public void addA2(A2 a2) {
        this.a2s.add(a2);
    }

}