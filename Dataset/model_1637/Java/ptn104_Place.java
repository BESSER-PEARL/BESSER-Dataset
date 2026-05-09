





import java.util.List;
import java.util.ArrayList;

public class ptn104_Place extends AbstractNode {






    private List<ptn104_Place> ptn104_places;


    public ptn104_Place(
    ) {
        super(
        );
        this.ptn104_places = new ArrayList<>();
    }

    public ptn104_Place(
        ArrayList<ptn104_Place> ptn104_places    ) {
        this.ptn104_places = ptn104_places;
    }


    public List<ptn104_Place> getPtn104_places() {
        return ptn104_places;
    }

    public void addPtn104_place(Ptn104_place ptn104_place) {
        this.ptn104_places.add(ptn104_place);
    }

}