





import java.util.List;
import java.util.ArrayList;

public class minuml1_Partition extends ModelElement {






    private minuml1_ModelElement minuml1_modelelement;




    private List<minuml1_ModelElement> minuml1_modelelements;


    public minuml1_Partition(
    ) {
        super(
        );
        this.minuml1_modelelements = new ArrayList<>();
    }

    public minuml1_Partition(
        ArrayList<minuml1_ModelElement> minuml1_modelelements    ) {
        this.minuml1_modelelements = minuml1_modelelements;
    }


    public minuml1_ModelElement getMinuml1_modelelement() {
        return minuml1_modelelement;
    }

    public void setMinuml1_modelelement(minuml1_ModelElement minuml1_modelelement) {
        this.minuml1_modelelement = minuml1_modelelement;
    }
    public List<minuml1_ModelElement> getMinuml1_modelelements() {
        return minuml1_modelelements;
    }

    public void addMinuml1_modelelement(Minuml1_modelelement minuml1_modelelement) {
        this.minuml1_modelelements.add(minuml1_modelelement);
    }

}