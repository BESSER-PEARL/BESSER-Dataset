





import java.util.List;
import java.util.ArrayList;

public class minuml1_Partition extends ModelElement {






    private minuml1_ActivityGraph minuml1_activitygraph;




    private List<minuml1_ModelElement> minuml1_modelelements;




    private minuml1_ModelElement minuml1_modelelement;


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


    public minuml1_ActivityGraph getMinuml1_activitygraph() {
        return minuml1_activitygraph;
    }

    public void setMinuml1_activitygraph(minuml1_ActivityGraph minuml1_activitygraph) {
        this.minuml1_activitygraph = minuml1_activitygraph;
    }
    public List<minuml1_ModelElement> getMinuml1_modelelements() {
        return minuml1_modelelements;
    }

    public void addMinuml1_modelelement(Minuml1_modelelement minuml1_modelelement) {
        this.minuml1_modelelements.add(minuml1_modelelement);
    }
    public minuml1_ModelElement getMinuml1_modelelement() {
        return minuml1_modelelement;
    }

    public void setMinuml1_modelelement(minuml1_ModelElement minuml1_modelelement) {
        this.minuml1_modelelement = minuml1_modelelement;
    }

}