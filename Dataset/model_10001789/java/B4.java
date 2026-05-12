





import java.util.List;
import java.util.ArrayList;

public class B4  {

    private int attB;





    private A4 a4;




    private List<C4> c4s;


    public B4(
        int attB    ) {
        this.attB = attB;
        this.c4s = new ArrayList<>();
    }

    public B4(
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

    public A4 getA4() {
        return a4;
    }

    public void setA4(A4 a4) {
        this.a4 = a4;
    }
    public List<C4> getC4s() {
        return c4s;
    }

    public void addC4(C4 c4) {
        this.c4s.add(c4);
    }

}