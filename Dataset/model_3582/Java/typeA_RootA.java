





import java.util.List;
import java.util.ArrayList;

public class typeA_RootA  {

    private String name;





    private List<typeA_ElementA> typea_elementas;


    public typeA_RootA(
        String name    ) {
        this.name = name;
        this.typea_elementas = new ArrayList<>();
    }

    public typeA_RootA(
        String name        ArrayList<typeA_ElementA> typea_elementas    ) {
        this.name = name;
        this.typea_elementas = typea_elementas;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<typeA_ElementA> getTypea_elementas() {
        return typea_elementas;
    }

    public void addTypea_elementa(Typea_elementa typea_elementa) {
        this.typea_elementas.add(typea_elementa);
    }

}