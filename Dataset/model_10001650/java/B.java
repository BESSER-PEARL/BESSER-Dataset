





import java.util.List;
import java.util.ArrayList;

public class B  {

    private String attB;





    private A a;




    private List<C> cs;


    public B(
        String attB    ) {
        this.attB = attB;
        this.cs = new ArrayList<>();
    }

    public B(
        String attB        ArrayList<C> cs    ) {
        this.attB = attB;
        this.cs = cs;
    }

    public String getAttb() {
        return attB;
    }

    public void setAttb(String attB) {
        this.attB = attB;
    }

    public A getA() {
        return a;
    }

    public void setA(A a) {
        this.a = a;
    }
    public List<C> getCs() {
        return cs;
    }

    public void addC(C c) {
        this.cs.add(c);
    }

}