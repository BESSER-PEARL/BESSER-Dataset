





import java.util.List;
import java.util.ArrayList;

public class crom_l1_Model  {






    private List<crom_l1_ModelElement> crom_l1_modelelements;


    public crom_l1_Model(
    ) {
        this.crom_l1_modelelements = new ArrayList<>();
    }

    public crom_l1_Model(
        ArrayList<crom_l1_ModelElement> crom_l1_modelelements    ) {
        this.crom_l1_modelelements = crom_l1_modelelements;
    }


    public List<crom_l1_ModelElement> getCrom_l1_modelelements() {
        return crom_l1_modelelements;
    }

    public void addCrom_l1_modelelement(Crom_l1_modelelement crom_l1_modelelement) {
        this.crom_l1_modelelements.add(crom_l1_modelelement);
    }

}