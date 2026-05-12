





import java.util.List;
import java.util.ArrayList;

public class B1  {

    private int attB;





    private List<C1> c1s;




    private A1 a1;




    private C1 c1;


    public B1(
        int attB    ) {
        this.attB = attB;
        this.c1s = new ArrayList<>();
    }

    public B1(
        int attB        ArrayList<C1> c1s    ) {
        this.attB = attB;
        this.c1s = c1s;
    }

    public int getAttb() {
        return attB;
    }

    public void setAttb(int attB) {
        this.attB = attB;
    }

    public List<C1> getC1s() {
        return c1s;
    }

    public void addC1(C1 c1) {
        this.c1s.add(c1);
    }
    public A1 getA1() {
        return a1;
    }

    public void setA1(A1 a1) {
        this.a1 = a1;
    }
    public C1 getC1() {
        return c1;
    }

    public void setC1(C1 c1) {
        this.c1 = c1;
    }

}