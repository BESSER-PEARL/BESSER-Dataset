





import java.util.List;
import java.util.ArrayList;

public class B_RootB  {






    private B_B b_b;




    private List<B_B> b_bs;


    public B_RootB(
    ) {
        this.b_bs = new ArrayList<>();
    }

    public B_RootB(
        ArrayList<B_B> b_bs    ) {
        this.b_bs = b_bs;
    }


    public B_B getB_b() {
        return b_b;
    }

    public void setB_b(B_B b_b) {
        this.b_b = b_b;
    }
    public List<B_B> getB_bs() {
        return b_bs;
    }

    public void addB_b(B_b b_b) {
        this.b_bs.add(b_b);
    }

}