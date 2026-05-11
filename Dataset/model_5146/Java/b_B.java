





import java.util.List;
import java.util.ArrayList;

public class b_B  {

    private boolean y;





    private List<b_A> b_as;




    private b_B b_b;


    public b_B(
        boolean y    ) {
        this.y = y;
        this.b_as = new ArrayList<>();
    }

    public b_B(
        boolean y        ArrayList<b_A> b_as    ) {
        this.y = y;
        this.b_as = b_as;
    }

    public boolean getY() {
        return y;
    }

    public void setY(boolean y) {
        this.y = y;
    }

    public List<b_A> getB_as() {
        return b_as;
    }

    public void addB_a(B_a b_a) {
        this.b_as.add(b_a);
    }
    public b_B getB_b() {
        return b_b;
    }

    public void setB_b(b_B b_b) {
        this.b_b = b_b;
    }

}