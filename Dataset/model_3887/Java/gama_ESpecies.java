





import java.util.List;
import java.util.ArrayList;

public class gama_ESpecies extends EGamaObject {

    private String skills;
    private String reflexList;
    private String init;





    private List<gama_EExperimentLink> gama_eexperimentlinks;




    private List<gama_EVariable> gama_evariables;




    private List<gama_EReflexLink> gama_ereflexlinks;




    private gama_EExperimentLink gama_eexperimentlink;




    private List<gama_ESubSpeciesLink> gama_esubspecieslinks;




    private gama_ESubSpeciesLink gama_esubspecieslink;




    private gama_EReflexLink gama_ereflexlink;




    private List<gama_EActionLink> gama_eactionlinks;




    private gama_EAspectLink gama_easpectlink;




    private gama_ESpecies gama_especies;




    private gama_EActionLink gama_eactionlink;




    private gama_ESubSpeciesLink gama_esubspecieslink;




    private List<gama_EAspectLink> gama_easpectlinks;




    private List<gama_ESubSpeciesLink> gama_esubspecieslinks;


    public gama_ESpecies(
        String skills,        String reflexList,        String init    ) {
        super(
        );
        this.skills = skills;
        this.reflexList = reflexList;
        this.init = init;
        this.gama_eexperimentlinks = new ArrayList<>();
        this.gama_evariables = new ArrayList<>();
        this.gama_ereflexlinks = new ArrayList<>();
        this.gama_esubspecieslinks = new ArrayList<>();
        this.gama_eactionlinks = new ArrayList<>();
        this.gama_easpectlinks = new ArrayList<>();
        this.gama_esubspecieslinks = new ArrayList<>();
    }

    public gama_ESpecies(
        String skills,        String reflexList,        String init        ArrayList<gama_EExperimentLink> gama_eexperimentlinks,        ArrayList<gama_EVariable> gama_evariables,        ArrayList<gama_EReflexLink> gama_ereflexlinks,        ArrayList<gama_ESubSpeciesLink> gama_esubspecieslinks,        ArrayList<gama_EActionLink> gama_eactionlinks,        ArrayList<gama_EAspectLink> gama_easpectlinks,        ArrayList<gama_ESubSpeciesLink> gama_esubspecieslinks    ) {
        this.skills = skills;
        this.reflexList = reflexList;
        this.init = init;
        this.gama_eexperimentlinks = gama_eexperimentlinks;
        this.gama_evariables = gama_evariables;
        this.gama_ereflexlinks = gama_ereflexlinks;
        this.gama_esubspecieslinks = gama_esubspecieslinks;
        this.gama_eactionlinks = gama_eactionlinks;
        this.gama_easpectlinks = gama_easpectlinks;
        this.gama_esubspecieslinks = gama_esubspecieslinks;
    }

    public String getSkills() {
        return skills;
    }

    public void setSkills(String skills) {
        this.skills = skills;
    }
    public String getReflexlist() {
        return reflexList;
    }

    public void setReflexlist(String reflexList) {
        this.reflexList = reflexList;
    }
    public String getInit() {
        return init;
    }

    public void setInit(String init) {
        this.init = init;
    }

    public List<gama_EExperimentLink> getGama_eexperimentlinks() {
        return gama_eexperimentlinks;
    }

    public void addGama_eexperimentlink(Gama_eexperimentlink gama_eexperimentlink) {
        this.gama_eexperimentlinks.add(gama_eexperimentlink);
    }
    public List<gama_EVariable> getGama_evariables() {
        return gama_evariables;
    }

    public void addGama_evariable(Gama_evariable gama_evariable) {
        this.gama_evariables.add(gama_evariable);
    }
    public List<gama_EReflexLink> getGama_ereflexlinks() {
        return gama_ereflexlinks;
    }

    public void addGama_ereflexlink(Gama_ereflexlink gama_ereflexlink) {
        this.gama_ereflexlinks.add(gama_ereflexlink);
    }
    public gama_EExperimentLink getGama_eexperimentlink() {
        return gama_eexperimentlink;
    }

    public void setGama_eexperimentlink(gama_EExperimentLink gama_eexperimentlink) {
        this.gama_eexperimentlink = gama_eexperimentlink;
    }
    public List<gama_ESubSpeciesLink> getGama_esubspecieslinks() {
        return gama_esubspecieslinks;
    }

    public void addGama_esubspecieslink(Gama_esubspecieslink gama_esubspecieslink) {
        this.gama_esubspecieslinks.add(gama_esubspecieslink);
    }
    public gama_ESubSpeciesLink getGama_esubspecieslink() {
        return gama_esubspecieslink;
    }

    public void setGama_esubspecieslink(gama_ESubSpeciesLink gama_esubspecieslink) {
        this.gama_esubspecieslink = gama_esubspecieslink;
    }
    public gama_EReflexLink getGama_ereflexlink() {
        return gama_ereflexlink;
    }

    public void setGama_ereflexlink(gama_EReflexLink gama_ereflexlink) {
        this.gama_ereflexlink = gama_ereflexlink;
    }
    public List<gama_EActionLink> getGama_eactionlinks() {
        return gama_eactionlinks;
    }

    public void addGama_eactionlink(Gama_eactionlink gama_eactionlink) {
        this.gama_eactionlinks.add(gama_eactionlink);
    }
    public gama_EAspectLink getGama_easpectlink() {
        return gama_easpectlink;
    }

    public void setGama_easpectlink(gama_EAspectLink gama_easpectlink) {
        this.gama_easpectlink = gama_easpectlink;
    }
    public gama_ESpecies getGama_especies() {
        return gama_especies;
    }

    public void setGama_especies(gama_ESpecies gama_especies) {
        this.gama_especies = gama_especies;
    }
    public gama_EActionLink getGama_eactionlink() {
        return gama_eactionlink;
    }

    public void setGama_eactionlink(gama_EActionLink gama_eactionlink) {
        this.gama_eactionlink = gama_eactionlink;
    }
    public gama_ESubSpeciesLink getGama_esubspecieslink() {
        return gama_esubspecieslink;
    }

    public void setGama_esubspecieslink(gama_ESubSpeciesLink gama_esubspecieslink) {
        this.gama_esubspecieslink = gama_esubspecieslink;
    }
    public List<gama_EAspectLink> getGama_easpectlinks() {
        return gama_easpectlinks;
    }

    public void addGama_easpectlink(Gama_easpectlink gama_easpectlink) {
        this.gama_easpectlinks.add(gama_easpectlink);
    }
    public List<gama_ESubSpeciesLink> getGama_esubspecieslinks() {
        return gama_esubspecieslinks;
    }

    public void addGama_esubspecieslink(Gama_esubspecieslink gama_esubspecieslink) {
        this.gama_esubspecieslinks.add(gama_esubspecieslink);
    }

}