





import java.util.List;
import java.util.ArrayList;

public class coCoMM_AttributeType  {

    private String name;
    private String id;





    private coCoMM_AttributeType cocomm_attributetype;




    private List<coCoMM_AttributeTypeElement> cocomm_attributetypeelements;




    private List<coCoMM_FeatureAttribute> cocomm_featureattributes;




    private coCoMM_FeatureAttribute cocomm_featureattribute;


    public coCoMM_AttributeType(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
        this.cocomm_attributetypeelements = new ArrayList<>();
        this.cocomm_featureattributes = new ArrayList<>();
    }

    public coCoMM_AttributeType(
        String name,        String id        ArrayList<coCoMM_AttributeTypeElement> cocomm_attributetypeelements,        ArrayList<coCoMM_FeatureAttribute> cocomm_featureattributes    ) {
        this.name = name;
        this.id = id;
        this.cocomm_attributetypeelements = cocomm_attributetypeelements;
        this.cocomm_featureattributes = cocomm_featureattributes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public coCoMM_AttributeType getCocomm_attributetype() {
        return cocomm_attributetype;
    }

    public void setCocomm_attributetype(coCoMM_AttributeType cocomm_attributetype) {
        this.cocomm_attributetype = cocomm_attributetype;
    }
    public List<coCoMM_AttributeTypeElement> getCocomm_attributetypeelements() {
        return cocomm_attributetypeelements;
    }

    public void addCocomm_attributetypeelement(Cocomm_attributetypeelement cocomm_attributetypeelement) {
        this.cocomm_attributetypeelements.add(cocomm_attributetypeelement);
    }
    public List<coCoMM_FeatureAttribute> getCocomm_featureattributes() {
        return cocomm_featureattributes;
    }

    public void addCocomm_featureattribute(Cocomm_featureattribute cocomm_featureattribute) {
        this.cocomm_featureattributes.add(cocomm_featureattribute);
    }
    public coCoMM_FeatureAttribute getCocomm_featureattribute() {
        return cocomm_featureattribute;
    }

    public void setCocomm_featureattribute(coCoMM_FeatureAttribute cocomm_featureattribute) {
        this.cocomm_featureattribute = cocomm_featureattribute;
    }

}