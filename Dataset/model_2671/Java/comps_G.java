





import java.util.List;
import java.util.ArrayList;

public class comps_G extends Named {






    private List<comps_H> comps_hs;


    public comps_G(
    ) {
        super(
        );
        this.comps_hs = new ArrayList<>();
    }

    public comps_G(
        ArrayList<comps_H> comps_hs    ) {
        this.comps_hs = comps_hs;
    }


    public List<comps_H> getComps_hs() {
        return comps_hs;
    }

    public void addComps_h(Comps_h comps_h) {
        this.comps_hs.add(comps_h);
    }

}