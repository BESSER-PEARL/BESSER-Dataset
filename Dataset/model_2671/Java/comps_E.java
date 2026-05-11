





import java.util.List;
import java.util.ArrayList;

public class comps_E extends Named, B {






    private List<comps_F> comps_fs;


    public comps_E(
    ) {
        super(
        );
        this.comps_fs = new ArrayList<>();
    }

    public comps_E(
        ArrayList<comps_F> comps_fs    ) {
        this.comps_fs = comps_fs;
    }


    public List<comps_F> getComps_fs() {
        return comps_fs;
    }

    public void addComps_f(Comps_f comps_f) {
        this.comps_fs.add(comps_f);
    }

}