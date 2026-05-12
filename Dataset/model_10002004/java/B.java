





import java.util.List;
import java.util.ArrayList;

public class B  {

    private int attB;





    private List<C> cs;




    private A a;


    public B(
        int attB    ) {
        this.attB = attB;
        this.cs = new ArrayList<>();
    }

    public B(
        int attB        ArrayList<C> cs    ) {
        this.attB = attB;
        this.cs = cs;
    }

    public int getAttb() {
        return attB;
    }

    public void setAttb(int attB) {
        this.attB = attB;
    }

    public List<C> getCs() {
        return cs;
    }

    public void addC(C c) {
        this.cs.add(c);
    }
    public A getA() {
        return a;
    }

    public void setA(A a) {
        this.a = a;
    }

}