





import java.util.List;
import java.util.ArrayList;

public class KM3_Package extends ModelElement {






    private List<KM3_ModelElement> km3_modelelements;




    private KM3_ModelElement km3_modelelement;




    private KM3_Metamodel km3_metamodel;




    private KM3_Metamodel km3_metamodel;


    public KM3_Package(
    ) {
        super(
        );
        this.km3_modelelements = new ArrayList<>();
    }

    public KM3_Package(
        ArrayList<KM3_ModelElement> km3_modelelements    ) {
        this.km3_modelelements = km3_modelelements;
    }


    public List<KM3_ModelElement> getKm3_modelelements() {
        return km3_modelelements;
    }

    public void addKm3_modelelement(Km3_modelelement km3_modelelement) {
        this.km3_modelelements.add(km3_modelelement);
    }
    public KM3_ModelElement getKm3_modelelement() {
        return km3_modelelement;
    }

    public void setKm3_modelelement(KM3_ModelElement km3_modelelement) {
        this.km3_modelelement = km3_modelelement;
    }
    public KM3_Metamodel getKm3_metamodel() {
        return km3_metamodel;
    }

    public void setKm3_metamodel(KM3_Metamodel km3_metamodel) {
        this.km3_metamodel = km3_metamodel;
    }
    public KM3_Metamodel getKm3_metamodel() {
        return km3_metamodel;
    }

    public void setKm3_metamodel(KM3_Metamodel km3_metamodel) {
        this.km3_metamodel = km3_metamodel;
    }

}