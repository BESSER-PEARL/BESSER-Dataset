





import java.util.List;
import java.util.ArrayList;

public class comps_B extends Named {






    private comps_A comps_a;




    private List<comps_G> comps_gs;


    public comps_B(
    ) {
        super(
        );
        this.comps_gs = new ArrayList<>();
    }

    public comps_B(
        ArrayList<comps_G> comps_gs    ) {
        this.comps_gs = comps_gs;
    }


    public comps_A getComps_a() {
        return comps_a;
    }

    public void setComps_a(comps_A comps_a) {
        this.comps_a = comps_a;
    }
    public List<comps_G> getComps_gs() {
        return comps_gs;
    }

    public void addComps_g(Comps_g comps_g) {
        this.comps_gs.add(comps_g);
    }

}