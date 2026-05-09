





import java.util.List;
import java.util.ArrayList;

public class ptntim101_Place extends AbstractNode {






    private List<ptntim101_Place> ptntim101_places;


    public ptntim101_Place(
    ) {
        super(
        );
        this.ptntim101_places = new ArrayList<>();
    }

    public ptntim101_Place(
        ArrayList<ptntim101_Place> ptntim101_places    ) {
        this.ptntim101_places = ptntim101_places;
    }


    public List<ptntim101_Place> getPtntim101_places() {
        return ptntim101_places;
    }

    public void addPtntim101_place(Ptntim101_place ptntim101_place) {
        this.ptntim101_places.add(ptntim101_place);
    }

}