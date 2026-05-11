





import java.util.List;
import java.util.ArrayList;

public class ABC_D  {






    private List<ABC_A> abc_as;


    public ABC_D(
    ) {
        this.abc_as = new ArrayList<>();
    }

    public ABC_D(
        ArrayList<ABC_A> abc_as    ) {
        this.abc_as = abc_as;
    }


    public List<ABC_A> getAbc_as() {
        return abc_as;
    }

    public void addAbc_a(Abc_a abc_a) {
        this.abc_as.add(abc_a);
    }

}