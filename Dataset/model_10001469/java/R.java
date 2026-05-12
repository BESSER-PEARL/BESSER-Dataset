





import java.util.List;
import java.util.ArrayList;

public class R  {






    private List<AA> aas;


    public R(
    ) {
        this.aas = new ArrayList<>();
    }

    public R(
        ArrayList<AA> aas    ) {
        this.aas = aas;
    }


    public List<AA> getAas() {
        return aas;
    }

    public void addAa(Aa aa) {
        this.aas.add(aa);
    }

}