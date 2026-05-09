





import java.util.List;
import java.util.ArrayList;

public class ptntim101_AbstractTransition extends AbstractNode {

    private String guard;





    private ptntim101_Place ptntim101_place;




    private List<ptntim101_Place> ptntim101_places;


    public ptntim101_AbstractTransition(
        String guard    ) {
        super(
        );
        this.guard = guard;
        this.ptntim101_places = new ArrayList<>();
    }

    public ptntim101_AbstractTransition(
        String guard        ArrayList<ptntim101_Place> ptntim101_places    ) {
        this.guard = guard;
        this.ptntim101_places = ptntim101_places;
    }

    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }

    public ptntim101_Place getPtntim101_place() {
        return ptntim101_place;
    }

    public void setPtntim101_place(ptntim101_Place ptntim101_place) {
        this.ptntim101_place = ptntim101_place;
    }
    public List<ptntim101_Place> getPtntim101_places() {
        return ptntim101_places;
    }

    public void addPtntim101_place(Ptntim101_place ptntim101_place) {
        this.ptntim101_places.add(ptntim101_place);
    }

}