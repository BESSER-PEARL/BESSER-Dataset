





import java.util.List;
import java.util.ArrayList;

public class a_Root  {

    private boolean visible;





    private List<a_A> a_as;




    private a_A a_a;


    public a_Root(
        boolean visible    ) {
        this.visible = visible;
        this.a_as = new ArrayList<>();
    }

    public a_Root(
        boolean visible        ArrayList<a_A> a_as    ) {
        this.visible = visible;
        this.a_as = a_as;
    }

    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public List<a_A> getA_as() {
        return a_as;
    }

    public void addA_a(A_a a_a) {
        this.a_as.add(a_a);
    }
    public a_A getA_a() {
        return a_a;
    }

    public void setA_a(a_A a_a) {
        this.a_a = a_a;
    }

}