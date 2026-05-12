





import java.util.List;
import java.util.ArrayList;

public class urml_PhaseSetEntry  {






    private urml_Phase urml_phase;




    private List<urml_EClass> urml_eclasss;




    private urml_EClass urml_eclass;


    public urml_PhaseSetEntry(
    ) {
        this.urml_eclasss = new ArrayList<>();
    }

    public urml_PhaseSetEntry(
        ArrayList<urml_EClass> urml_eclasss    ) {
        this.urml_eclasss = urml_eclasss;
    }


    public urml_Phase getUrml_phase() {
        return urml_phase;
    }

    public void setUrml_phase(urml_Phase urml_phase) {
        this.urml_phase = urml_phase;
    }
    public List<urml_EClass> getUrml_eclasss() {
        return urml_eclasss;
    }

    public void addUrml_eclass(Urml_eclass urml_eclass) {
        this.urml_eclasss.add(urml_eclass);
    }
    public urml_EClass getUrml_eclass() {
        return urml_eclass;
    }

    public void setUrml_eclass(urml_EClass urml_eclass) {
        this.urml_eclass = urml_eclass;
    }

}