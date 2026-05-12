





import java.util.List;
import java.util.ArrayList;

public class B  {

    private String attb;





    private List<C> cs;




    private A a;


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