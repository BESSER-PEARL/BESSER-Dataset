





import java.util.List;
import java.util.ArrayList;

public class sgen_FeatureTypeLibrary  {

    private String name;





    private List<sgen_FeatureType> sgen_featuretypes;




    private sgen_FeatureType sgen_featuretype;


    public sgen_FeatureTypeLibrary(
        String name    ) {
        this.name = name;
        this.sgen_featuretypes = new ArrayList<>();
    }

    public sgen_FeatureTypeLibrary(
        String name        ArrayList<sgen_FeatureType> sgen_featuretypes    ) {
        this.name = name;
        this.sgen_featuretypes = sgen_featuretypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sgen_FeatureType> getSgen_featuretypes() {
        return sgen_featuretypes;
    }

    public void addSgen_featuretype(Sgen_featuretype sgen_featuretype) {
        this.sgen_featuretypes.add(sgen_featuretype);
    }
    public sgen_FeatureType getSgen_featuretype() {
        return sgen_featuretype;
    }

    public void setSgen_featuretype(sgen_FeatureType sgen_featuretype) {
        this.sgen_featuretype = sgen_featuretype;
    }

}