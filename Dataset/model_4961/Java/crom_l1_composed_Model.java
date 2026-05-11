





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_Model  {






    private List<crom_l1_composed_ModelElement> crom_l1_composed_modelelements;


    public crom_l1_composed_Model(
    ) {
        this.crom_l1_composed_modelelements = new ArrayList<>();
    }

    public crom_l1_composed_Model(
        ArrayList<crom_l1_composed_ModelElement> crom_l1_composed_modelelements    ) {
        this.crom_l1_composed_modelelements = crom_l1_composed_modelelements;
    }


    public List<crom_l1_composed_ModelElement> getCrom_l1_composed_modelelements() {
        return crom_l1_composed_modelelements;
    }

    public void addCrom_l1_composed_modelelement(Crom_l1_composed_modelelement crom_l1_composed_modelelement) {
        this.crom_l1_composed_modelelements.add(crom_l1_composed_modelelement);
    }

}