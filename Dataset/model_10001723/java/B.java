





import java.util.List;
import java.util.ArrayList;

public class B  {

    private String attb;





    private A a;




    private List<C> cs;


    public B(
        String attb    ) {
        this.attb = attb;
        this.cs = new ArrayList<>();
    }

    public B(
        String attb        ArrayList<C> cs    ) {
        this.attb = attb;
        this.cs = cs;
    }

    public String getAttb() {
        return attb;
    }

    public void setAttb(String attb) {
        this.attb = attb;
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