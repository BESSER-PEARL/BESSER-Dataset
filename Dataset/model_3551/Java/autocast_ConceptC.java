





import java.util.List;
import java.util.ArrayList;

public class autocast_ConceptC  {






    private List<autocast_ConceptA> autocast_conceptas;


    public autocast_ConceptC(
    ) {
        this.autocast_conceptas = new ArrayList<>();
    }

    public autocast_ConceptC(
        ArrayList<autocast_ConceptA> autocast_conceptas    ) {
        this.autocast_conceptas = autocast_conceptas;
    }


    public List<autocast_ConceptA> getAutocast_conceptas() {
        return autocast_conceptas;
    }

    public void addAutocast_concepta(Autocast_concepta autocast_concepta) {
        this.autocast_conceptas.add(autocast_concepta);
    }

}