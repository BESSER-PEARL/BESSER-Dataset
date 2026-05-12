





import java.util.List;
import java.util.ArrayList;

public class B2  {

    private int attB;





    private A2 a2;




    private List<C4> c4s;


    public B2(
        int attB    ) {
        this.attB = attB;
        this.c4s = new ArrayList<>();
    }

    public B2(
        int attB        ArrayList<C4> c4s    ) {
        this.attB = attB;
        this.c4s = c4s;
    }

    public int getAttb() {
        return attB;
    }

    public void setAttb(int attB) {
        this.attB = attB;
    }

    public A2 getA2() {
        return a2;
    }

    public void setA2(A2 a2) {
        this.a2 = a2;
    }
    public List<C4> getC4s() {
        return c4s;
    }

    public void addC4(C4 c4) {
        this.c4s.add(c4);
    }

}