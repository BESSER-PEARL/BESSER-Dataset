





import java.util.List;
import java.util.ArrayList;

public class camel_provider_Feature  {

    private String name;





    private List<Feature> features;




    private FeatCardinality featcardinality;




    private List<Clone> clones;




    private List<Attribute> attributes;


    public camel_provider_Feature(
        String name    ) {
        this.name = name;
        this.features = new ArrayList<>();
        this.clones = new ArrayList<>();
        this.attributes = new ArrayList<>();
    }

    public camel_provider_Feature(
        String name        ArrayList<Feature> features,        ArrayList<Clone> clones,        ArrayList<Attribute> attributes    ) {
        this.name = name;
        this.features = features;
        this.clones = clones;
        this.attributes = attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Feature> getFeatures() {
        return features;
    }

    public void addFeature(Feature feature) {
        this.features.add(feature);
    }
    public FeatCardinality getFeatcardinality() {
        return featcardinality;
    }

    public void setFeatcardinality(FeatCardinality featcardinality) {
        this.featcardinality = featcardinality;
    }
    public List<Clone> getClones() {
        return clones;
    }

    public void addClone(Clone clone) {
        this.clones.add(clone);
    }
    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }

}