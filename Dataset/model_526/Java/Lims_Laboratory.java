





import java.util.List;
import java.util.ArrayList;

public class Lims_Laboratory  {






    private Lims_Family lims_family;




    private List<Lims_Family> lims_familys;


    public Lims_Laboratory(
    ) {
        this.lims_familys = new ArrayList<>();
    }

    public Lims_Laboratory(
        ArrayList<Lims_Family> lims_familys    ) {
        this.lims_familys = lims_familys;
    }


    public Lims_Family getLims_family() {
        return lims_family;
    }

    public void setLims_family(Lims_Family lims_family) {
        this.lims_family = lims_family;
    }
    public List<Lims_Family> getLims_familys() {
        return lims_familys;
    }

    public void addLims_family(Lims_family lims_family) {
        this.lims_familys.add(lims_family);
    }

}