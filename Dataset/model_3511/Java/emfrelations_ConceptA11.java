





import java.util.List;
import java.util.ArrayList;

public class emfrelations_ConceptA11  {






    private List<emfrelations_ConceptB11> emfrelations_conceptb11s;


    public emfrelations_ConceptA11(
    ) {
        this.emfrelations_conceptb11s = new ArrayList<>();
    }

    public emfrelations_ConceptA11(
        ArrayList<emfrelations_ConceptB11> emfrelations_conceptb11s    ) {
        this.emfrelations_conceptb11s = emfrelations_conceptb11s;
    }


    public List<emfrelations_ConceptB11> getEmfrelations_conceptb11s() {
        return emfrelations_conceptb11s;
    }

    public void addEmfrelations_conceptb11(Emfrelations_conceptb11 emfrelations_conceptb11) {
        this.emfrelations_conceptb11s.add(emfrelations_conceptb11);
    }

}