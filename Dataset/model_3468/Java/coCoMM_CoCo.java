





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CoCo  {

    private String name;
    private String id;
    private String configScenario;





    private List<coCoMM_FeatureModel> cocomm_featuremodels;




    private List<coCoMM_AttributeType> cocomm_attributetypes;


    public coCoMM_CoCo(
        String name,        String id,        String configScenario    ) {
        this.name = name;
        this.id = id;
        this.configScenario = configScenario;
        this.cocomm_featuremodels = new ArrayList<>();
        this.cocomm_attributetypes = new ArrayList<>();
    }

    public coCoMM_CoCo(
        String name,        String id,        String configScenario        ArrayList<coCoMM_FeatureModel> cocomm_featuremodels,        ArrayList<coCoMM_AttributeType> cocomm_attributetypes    ) {
        this.name = name;
        this.id = id;
        this.configScenario = configScenario;
        this.cocomm_featuremodels = cocomm_featuremodels;
        this.cocomm_attributetypes = cocomm_attributetypes;
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
    public String getConfigscenario() {
        return configScenario;
    }

    public void setConfigscenario(String configScenario) {
        this.configScenario = configScenario;
    }

    public List<coCoMM_FeatureModel> getCocomm_featuremodels() {
        return cocomm_featuremodels;
    }

    public void addCocomm_featuremodel(Cocomm_featuremodel cocomm_featuremodel) {
        this.cocomm_featuremodels.add(cocomm_featuremodel);
    }
    public List<coCoMM_AttributeType> getCocomm_attributetypes() {
        return cocomm_attributetypes;
    }

    public void addCocomm_attributetype(Cocomm_attributetype cocomm_attributetype) {
        this.cocomm_attributetypes.add(cocomm_attributetype);
    }

}