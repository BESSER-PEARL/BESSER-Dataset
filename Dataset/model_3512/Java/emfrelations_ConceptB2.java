





import java.util.List;
import java.util.ArrayList;

public class emfrelations_ConceptB2  {






    private List<emfrelations_ConceptA2> emfrelations_concepta2s;




    private emfrelations_ConceptA2 emfrelations_concepta2;


    public emfrelations_ConceptB2(
    ) {
        this.emfrelations_concepta2s = new ArrayList<>();
    }

    public emfrelations_ConceptB2(
        ArrayList<emfrelations_ConceptA2> emfrelations_concepta2s    ) {
        this.emfrelations_concepta2s = emfrelations_concepta2s;
    }


    public List<emfrelations_ConceptA2> getEmfrelations_concepta2s() {
        return emfrelations_concepta2s;
    }

    public void addEmfrelations_concepta2(Emfrelations_concepta2 emfrelations_concepta2) {
        this.emfrelations_concepta2s.add(emfrelations_concepta2);
    }
    public emfrelations_ConceptA2 getEmfrelations_concepta2() {
        return emfrelations_concepta2;
    }

    public void setEmfrelations_concepta2(emfrelations_ConceptA2 emfrelations_concepta2) {
        this.emfrelations_concepta2 = emfrelations_concepta2;
    }

}