





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_ResourceUsage  {






    private List<GRM_Resource> grm_resources;




    private GRM_MARTE_NamedElement grm_marte_namedelement;




    private List<NFP_Duration> nfp_durations;




    private List<GRM_ResourceUsage> grm_resourceusages;


    public MARTE_GRM_ResourceUsage(
    ) {
        this.grm_resources = new ArrayList<>();
        this.nfp_durations = new ArrayList<>();
        this.grm_resourceusages = new ArrayList<>();
    }

    public MARTE_GRM_ResourceUsage(
        ArrayList<GRM_Resource> grm_resources,        ArrayList<NFP_Duration> nfp_durations,        ArrayList<GRM_ResourceUsage> grm_resourceusages    ) {
        this.grm_resources = grm_resources;
        this.nfp_durations = nfp_durations;
        this.grm_resourceusages = grm_resourceusages;
    }


    public List<GRM_Resource> getGrm_resources() {
        return grm_resources;
    }

    public void addGrm_resource(Grm_resource grm_resource) {
        this.grm_resources.add(grm_resource);
    }
    public GRM_MARTE_NamedElement getGrm_marte_namedelement() {
        return grm_marte_namedelement;
    }

    public void setGrm_marte_namedelement(GRM_MARTE_NamedElement grm_marte_namedelement) {
        this.grm_marte_namedelement = grm_marte_namedelement;
    }
    public List<NFP_Duration> getNfp_durations() {
        return nfp_durations;
    }

    public void addNfp_duration(Nfp_duration nfp_duration) {
        this.nfp_durations.add(nfp_duration);
    }
    public List<GRM_ResourceUsage> getGrm_resourceusages() {
        return grm_resourceusages;
    }

    public void addGrm_resourceusage(Grm_resourceusage grm_resourceusage) {
        this.grm_resourceusages.add(grm_resourceusage);
    }

}