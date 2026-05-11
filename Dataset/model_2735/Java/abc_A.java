





import java.util.List;
import java.util.ArrayList;

public class abc_A  {

    private int x;





    private abc_C abc_c;




    private List<abc_B> abc_bs;




    private abc_B abc_b;


    public abc_A(
        int x    ) {
        this.x = x;
        this.abc_bs = new ArrayList<>();
    }

    public abc_A(
        int x        ArrayList<abc_B> abc_bs    ) {
        this.x = x;
        this.abc_bs = abc_bs;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public abc_C getAbc_c() {
        return abc_c;
    }

    public void setAbc_c(abc_C abc_c) {
        this.abc_c = abc_c;
    }
    public List<abc_B> getAbc_bs() {
        return abc_bs;
    }

    public void addAbc_b(Abc_b abc_b) {
        this.abc_bs.add(abc_b);
    }
    public abc_B getAbc_b() {
        return abc_b;
    }

    public void setAbc_b(abc_B abc_b) {
        this.abc_b = abc_b;
    }

}