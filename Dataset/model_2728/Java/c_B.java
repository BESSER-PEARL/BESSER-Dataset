





import java.util.List;
import java.util.ArrayList;

public class c_B  {

    private boolean y;
    private float c;





    private List<c_A> c_as;




    private c_C c_c;




    private c_C c_c;




    private c_B c_b;




    private c_A c_a;


    public c_B(
        boolean y,        float c    ) {
        this.y = y;
        this.c = c;
        this.c_as = new ArrayList<>();
    }

    public c_B(
        boolean y,        float c        ArrayList<c_A> c_as    ) {
        this.y = y;
        this.c = c;
        this.c_as = c_as;
    }

    public boolean getY() {
        return y;
    }

    public void setY(boolean y) {
        this.y = y;
    }
    public float getC() {
        return c;
    }

    public void setC(float c) {
        this.c = c;
    }

    public List<c_A> getC_as() {
        return c_as;
    }

    public void addC_a(C_a c_a) {
        this.c_as.add(c_a);
    }
    public c_C getC_c() {
        return c_c;
    }

    public void setC_c(c_C c_c) {
        this.c_c = c_c;
    }
    public c_C getC_c() {
        return c_c;
    }

    public void setC_c(c_C c_c) {
        this.c_c = c_c;
    }
    public c_B getC_b() {
        return c_b;
    }

    public void setC_b(c_B c_b) {
        this.c_b = c_b;
    }
    public c_A getC_a() {
        return c_a;
    }

    public void setC_a(c_A c_a) {
        this.c_a = c_a;
    }

}