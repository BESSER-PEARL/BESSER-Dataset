





import java.util.List;
import java.util.ArrayList;

public class EFM_NodeFeature extends NodeFeatureElement {

    private String name;





    private List<EFM_Attribute> efm_attributes;




    private EFM_FeatCardinality efm_featcardinality;




    private EFM_Feature efm_feature;


    public EFM_NodeFeature(
        String name    ) {
        super(
        );
        this.name = name;
        this.efm_attributes = new ArrayList<>();
    }

    public EFM_NodeFeature(
        String name        ArrayList<EFM_Attribute> efm_attributes    ) {
        this.name = name;
        this.efm_attributes = efm_attributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<EFM_Attribute> getEfm_attributes() {
        return efm_attributes;
    }

    public void addEfm_attribute(Efm_attribute efm_attribute) {
        this.efm_attributes.add(efm_attribute);
    }
    public EFM_FeatCardinality getEfm_featcardinality() {
        return efm_featcardinality;
    }

    public void setEfm_featcardinality(EFM_FeatCardinality efm_featcardinality) {
        this.efm_featcardinality = efm_featcardinality;
    }
    public EFM_Feature getEfm_feature() {
        return efm_feature;
    }

    public void setEfm_feature(EFM_Feature efm_feature) {
        this.efm_feature = efm_feature;
    }

}