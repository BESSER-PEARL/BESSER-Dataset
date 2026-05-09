





import java.util.List;
import java.util.ArrayList;

public class ptn_AbstractTransition extends AbstractNode {

    private String guard;





    private List<ptn_Place> ptn_places;




    private ptn_Place ptn_place;


    public ptn_AbstractTransition(
        String guard    ) {
        super(
        );
        this.guard = guard;
        this.ptn_places = new ArrayList<>();
    }

    public ptn_AbstractTransition(
        String guard        ArrayList<ptn_Place> ptn_places    ) {
        this.guard = guard;
        this.ptn_places = ptn_places;
    }

    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }

    public List<ptn_Place> getPtn_places() {
        return ptn_places;
    }

    public void addPtn_place(Ptn_place ptn_place) {
        this.ptn_places.add(ptn_place);
    }
    public ptn_Place getPtn_place() {
        return ptn_place;
    }

    public void setPtn_place(ptn_Place ptn_place) {
        this.ptn_place = ptn_place;
    }

}