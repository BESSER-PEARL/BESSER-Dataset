





import java.util.List;
import java.util.ArrayList;

public class A1  {

    private int d;
    private None c;
    private boolean b;





    private List<B1> b1s;


    public A1(
        int d,        None c,        boolean b    ) {
        this.d = d;
        this.c = c;
        this.b = b;
        this.b1s = new ArrayList<>();
    }

    public A1(
        int d,        None c,        boolean b        ArrayList<B1> b1s    ) {
        this.d = d;
        this.c = c;
        this.b = b;
        this.b1s = b1s;
    }

    public int getD() {
        return d;
    }

    public void setD(int d) {
        this.d = d;
    }
    public None getC() {
        return c;
    }

    public void setC(None c) {
        this.c = c;
    }
    public boolean getB() {
        return b;
    }

    public void setB(boolean b) {
        this.b = b;
    }

    public List<B1> getB1s() {
        return b1s;
    }

    public void addB1(B1 b1) {
        this.b1s.add(b1);
    }

}