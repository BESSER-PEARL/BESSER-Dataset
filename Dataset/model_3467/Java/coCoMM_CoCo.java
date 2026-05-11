





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CoCo  {

    private String configScenario;





    private List<coCoMM_AttributeType> cocomm_attributetypes;




    private List<coCoMM_FeatureModel> cocomm_featuremodels;


    public coCoMM_CoCo(
        String configScenario    ) {
        this.configScenario = configScenario;
        this.cocomm_attributetypes = new ArrayList<>();
        this.cocomm_featuremodels = new ArrayList<>();
    }

    public coCoMM_CoCo(
        String configScenario        ArrayList<coCoMM_AttributeType> cocomm_attributetypes,        ArrayList<coCoMM_FeatureModel> cocomm_featuremodels    ) {
        this.configScenario = configScenario;
        this.cocomm_attributetypes = cocomm_attributetypes;
        this.cocomm_featuremodels = cocomm_featuremodels;
    }

    public String getConfigscenario() {
        return configScenario;
    }

    public void setConfigscenario(String configScenario) {
        this.configScenario = configScenario;
    }

    public List<coCoMM_AttributeType> getCocomm_attributetypes() {
        return cocomm_attributetypes;
    }

    public void addCocomm_attributetype(Cocomm_attributetype cocomm_attributetype) {
        this.cocomm_attributetypes.add(cocomm_attributetype);
    }
    public List<coCoMM_FeatureModel> getCocomm_featuremodels() {
        return cocomm_featuremodels;
    }

    public void addCocomm_featuremodel(Cocomm_featuremodel cocomm_featuremodel) {
        this.cocomm_featuremodels.add(cocomm_featuremodel);
    }

}