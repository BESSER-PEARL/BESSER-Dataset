





import java.util.List;
import java.util.ArrayList;

public class Lims_Laboratory  {






    private Lims_Sequencer lims_sequencer;




    private List<Lims_Family> lims_familys;




    private List<Lims_Sequencer> lims_sequencers;




    private Lims_Family lims_family;


    public Lims_Laboratory(
    ) {
        this.lims_familys = new ArrayList<>();
        this.lims_sequencers = new ArrayList<>();
    }

    public Lims_Laboratory(
        ArrayList<Lims_Family> lims_familys,        ArrayList<Lims_Sequencer> lims_sequencers    ) {
        this.lims_familys = lims_familys;
        this.lims_sequencers = lims_sequencers;
    }


    public Lims_Sequencer getLims_sequencer() {
        return lims_sequencer;
    }

    public void setLims_sequencer(Lims_Sequencer lims_sequencer) {
        this.lims_sequencer = lims_sequencer;
    }
    public List<Lims_Family> getLims_familys() {
        return lims_familys;
    }

    public void addLims_family(Lims_family lims_family) {
        this.lims_familys.add(lims_family);
    }
    public List<Lims_Sequencer> getLims_sequencers() {
        return lims_sequencers;
    }

    public void addLims_sequencer(Lims_sequencer lims_sequencer) {
        this.lims_sequencers.add(lims_sequencer);
    }
    public Lims_Family getLims_family() {
        return lims_family;
    }

    public void setLims_family(Lims_Family lims_family) {
        this.lims_family = lims_family;
    }

}