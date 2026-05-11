





import java.util.List;
import java.util.ArrayList;

public class emfrelations_ConceptB3  {






    private emfrelations_ConceptA3 emfrelations_concepta3;




    private List<emfrelations_ConceptA3> emfrelations_concepta3s;


    public emfrelations_ConceptB3(
    ) {
        this.emfrelations_concepta3s = new ArrayList<>();
    }

    public emfrelations_ConceptB3(
        ArrayList<emfrelations_ConceptA3> emfrelations_concepta3s    ) {
        this.emfrelations_concepta3s = emfrelations_concepta3s;
    }


    public emfrelations_ConceptA3 getEmfrelations_concepta3() {
        return emfrelations_concepta3;
    }

    public void setEmfrelations_concepta3(emfrelations_ConceptA3 emfrelations_concepta3) {
        this.emfrelations_concepta3 = emfrelations_concepta3;
    }
    public List<emfrelations_ConceptA3> getEmfrelations_concepta3s() {
        return emfrelations_concepta3s;
    }

    public void addEmfrelations_concepta3(Emfrelations_concepta3 emfrelations_concepta3) {
        this.emfrelations_concepta3s.add(emfrelations_concepta3);
    }

}