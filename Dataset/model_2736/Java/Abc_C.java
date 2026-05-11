





import java.util.List;
import java.util.ArrayList;

public class Abc_C  {






    private List<Abc_classB> abc_classbs;




    private Abc_A abc_a;


    public Abc_C(
    ) {
        this.abc_classbs = new ArrayList<>();
    }

    public Abc_C(
        ArrayList<Abc_classB> abc_classbs    ) {
        this.abc_classbs = abc_classbs;
    }


    public List<Abc_classB> getAbc_classbs() {
        return abc_classbs;
    }

    public void addAbc_classb(Abc_classb abc_classb) {
        this.abc_classbs.add(abc_classb);
    }
    public Abc_A getAbc_a() {
        return abc_a;
    }

    public void setAbc_a(Abc_A abc_a) {
        this.abc_a = abc_a;
    }

}