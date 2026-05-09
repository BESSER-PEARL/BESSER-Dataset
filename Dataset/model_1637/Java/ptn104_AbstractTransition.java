





import java.util.List;
import java.util.ArrayList;

public class ptn104_AbstractTransition extends AbstractNode {

    private String guard;





    private List<ptn104_Place> ptn104_places;




    private ptn104_Place ptn104_place;


    public ptn104_AbstractTransition(
        String guard    ) {
        super(
        );
        this.guard = guard;
        this.ptn104_places = new ArrayList<>();
    }

    public ptn104_AbstractTransition(
        String guard        ArrayList<ptn104_Place> ptn104_places    ) {
        this.guard = guard;
        this.ptn104_places = ptn104_places;
    }

    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }

    public List<ptn104_Place> getPtn104_places() {
        return ptn104_places;
    }

    public void addPtn104_place(Ptn104_place ptn104_place) {
        this.ptn104_places.add(ptn104_place);
    }
    public ptn104_Place getPtn104_place() {
        return ptn104_place;
    }

    public void setPtn104_place(ptn104_Place ptn104_place) {
        this.ptn104_place = ptn104_place;
    }

}