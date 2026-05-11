





import java.util.List;
import java.util.ArrayList;

public class gama_EExperiment extends ESpecies {






    private List<gama_EMonitor> gama_emonitors;




    private gama_EExperimentLink gama_eexperimentlink;




    private List<gama_EParameter> gama_eparameters;




    private gama_EExperimentLink gama_eexperimentlink;


    public gama_EExperiment(
    ) {
        super(
        );
        this.gama_emonitors = new ArrayList<>();
        this.gama_eparameters = new ArrayList<>();
    }

    public gama_EExperiment(
        ArrayList<gama_EMonitor> gama_emonitors,        ArrayList<gama_EParameter> gama_eparameters    ) {
        this.gama_emonitors = gama_emonitors;
        this.gama_eparameters = gama_eparameters;
    }


    public List<gama_EMonitor> getGama_emonitors() {
        return gama_emonitors;
    }

    public void addGama_emonitor(Gama_emonitor gama_emonitor) {
        this.gama_emonitors.add(gama_emonitor);
    }
    public gama_EExperimentLink getGama_eexperimentlink() {
        return gama_eexperimentlink;
    }

    public void setGama_eexperimentlink(gama_EExperimentLink gama_eexperimentlink) {
        this.gama_eexperimentlink = gama_eexperimentlink;
    }
    public List<gama_EParameter> getGama_eparameters() {
        return gama_eparameters;
    }

    public void addGama_eparameter(Gama_eparameter gama_eparameter) {
        this.gama_eparameters.add(gama_eparameter);
    }
    public gama_EExperimentLink getGama_eexperimentlink() {
        return gama_eexperimentlink;
    }

    public void setGama_eexperimentlink(gama_EExperimentLink gama_eexperimentlink) {
        this.gama_eexperimentlink = gama_eexperimentlink;
    }

}