





import java.util.List;
import java.util.ArrayList;

public class B  {

    private String altB;





    private List<C> cs;




    private A a;


    public B(
        String altB    ) {
        this.altB = altB;
        this.cs = new ArrayList<>();
    }

    public B(
        String altB        ArrayList<C> cs    ) {
        this.altB = altB;
        this.cs = cs;
    }

    public String getAltb() {
        return altB;
    }

    public void setAltb(String altB) {
        this.altB = altB;
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