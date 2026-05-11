





import java.util.List;
import java.util.ArrayList;

public class scxml_ServiceTemplate  {

    private String exmode;
    private String version;
    private String profile;
    private String name;
    private String xmlns;





    private List<scxml_Parallel> scxml_parallels;




    private List<scxml_DataModel> scxml_datamodels;




    private List<scxml_FinalState> scxml_finalstates;




    private List<scxml_Transition> scxml_transitions;


    public scxml_ServiceTemplate(
        String exmode,        String version,        String profile,        String name,        String xmlns    ) {
        this.exmode = exmode;
        this.version = version;
        this.profile = profile;
        this.name = name;
        this.xmlns = xmlns;
        this.scxml_parallels = new ArrayList<>();
        this.scxml_datamodels = new ArrayList<>();
        this.scxml_finalstates = new ArrayList<>();
        this.scxml_transitions = new ArrayList<>();
    }

    public scxml_ServiceTemplate(
        String exmode,        String version,        String profile,        String name,        String xmlns        ArrayList<scxml_Parallel> scxml_parallels,        ArrayList<scxml_DataModel> scxml_datamodels,        ArrayList<scxml_FinalState> scxml_finalstates,        ArrayList<scxml_Transition> scxml_transitions    ) {
        this.exmode = exmode;
        this.version = version;
        this.profile = profile;
        this.name = name;
        this.xmlns = xmlns;
        this.scxml_parallels = scxml_parallels;
        this.scxml_datamodels = scxml_datamodels;
        this.scxml_finalstates = scxml_finalstates;
        this.scxml_transitions = scxml_transitions;
    }

    public String getExmode() {
        return exmode;
    }

    public void setExmode(String exmode) {
        this.exmode = exmode;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getXmlns() {
        return xmlns;
    }

    public void setXmlns(String xmlns) {
        this.xmlns = xmlns;
    }

    public List<scxml_Parallel> getScxml_parallels() {
        return scxml_parallels;
    }

    public void addScxml_parallel(Scxml_parallel scxml_parallel) {
        this.scxml_parallels.add(scxml_parallel);
    }
    public List<scxml_DataModel> getScxml_datamodels() {
        return scxml_datamodels;
    }

    public void addScxml_datamodel(Scxml_datamodel scxml_datamodel) {
        this.scxml_datamodels.add(scxml_datamodel);
    }
    public List<scxml_FinalState> getScxml_finalstates() {
        return scxml_finalstates;
    }

    public void addScxml_finalstate(Scxml_finalstate scxml_finalstate) {
        this.scxml_finalstates.add(scxml_finalstate);
    }
    public List<scxml_Transition> getScxml_transitions() {
        return scxml_transitions;
    }

    public void addScxml_transition(Scxml_transition scxml_transition) {
        this.scxml_transitions.add(scxml_transition);
    }

}