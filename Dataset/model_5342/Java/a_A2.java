





import java.util.List;
import java.util.ArrayList;

public class a_A2  {






    private List<a_A1> a_a1s;


    public a_A2(
    ) {
        this.a_a1s = new ArrayList<>();
    }

    public a_A2(
        ArrayList<a_A1> a_a1s    ) {
        this.a_a1s = a_a1s;
    }


    public List<a_A1> getA_a1s() {
        return a_a1s;
    }

    public void addA_a1(A_a1 a_a1) {
        this.a_a1s.add(a_a1);
    }

}