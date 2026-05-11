





import java.util.List;
import java.util.ArrayList;

public class Kasu2_Root  {






    private List<Kasu2_ClassA> kasu2_classas;




    private Kasu2_ClassA kasu2_classa;


    public Kasu2_Root(
    ) {
        this.kasu2_classas = new ArrayList<>();
    }

    public Kasu2_Root(
        ArrayList<Kasu2_ClassA> kasu2_classas    ) {
        this.kasu2_classas = kasu2_classas;
    }


    public List<Kasu2_ClassA> getKasu2_classas() {
        return kasu2_classas;
    }

    public void addKasu2_classa(Kasu2_classa kasu2_classa) {
        this.kasu2_classas.add(kasu2_classa);
    }
    public Kasu2_ClassA getKasu2_classa() {
        return kasu2_classa;
    }

    public void setKasu2_classa(Kasu2_ClassA kasu2_classa) {
        this.kasu2_classa = kasu2_classa;
    }

}