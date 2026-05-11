





import java.util.List;
import java.util.ArrayList;

public class abc_A  {






    private List<abc_B> abc_bs;


    public abc_A(
    ) {
        this.abc_bs = new ArrayList<>();
    }

    public abc_A(
        ArrayList<abc_B> abc_bs    ) {
        this.abc_bs = abc_bs;
    }


    public List<abc_B> getAbc_bs() {
        return abc_bs;
    }

    public void addAbc_b(Abc_b abc_b) {
        this.abc_bs.add(abc_b);
    }

}