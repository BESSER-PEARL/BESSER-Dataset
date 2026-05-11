





import java.util.List;
import java.util.ArrayList;

public class spinefm_SystemActionModel_ActionOnFM extends SystemAction {

    private String fma;





    private ConfigurationProcessStep configurationprocessstep;




    private FeatureModel featuremodel;


    public spinefm_SystemActionModel_ActionOnFM(
        String fma    ) {
        super(
        );
        this.fma = fma;
    }


    public String getFma() {
        return fma;
    }

    public void setFma(String fma) {
        this.fma = fma;
    }

    public ConfigurationProcessStep getConfigurationprocessstep() {
        return configurationprocessstep;
    }

    public void setConfigurationprocessstep(ConfigurationProcessStep configurationprocessstep) {
        this.configurationprocessstep = configurationprocessstep;
    }
    public FeatureModel getFeaturemodel() {
        return featuremodel;
    }

    public void setFeaturemodel(FeatureModel featuremodel) {
        this.featuremodel = featuremodel;
    }

}