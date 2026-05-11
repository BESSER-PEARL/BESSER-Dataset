





import java.util.List;
import java.util.ArrayList;

public class refinher_D  {






    private List<refinher_E> refinher_es;


    public refinher_D(
    ) {
        this.refinher_es = new ArrayList<>();
    }

    public refinher_D(
        ArrayList<refinher_E> refinher_es    ) {
        this.refinher_es = refinher_es;
    }


    public List<refinher_E> getRefinher_es() {
        return refinher_es;
    }

    public void addRefinher_e(Refinher_e refinher_e) {
        this.refinher_es.add(refinher_e);
    }

}