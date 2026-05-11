





import java.util.List;
import java.util.ArrayList;

public class FCORE_Softgoal  {

    private String name;
    private String weighting;





    private FCORE_FeatureModel fcore_featuremodel;


    public FCORE_Softgoal(
        String name,        String weighting    ) {
        this.name = name;
        this.weighting = weighting;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWeighting() {
        return weighting;
    }

    public void setWeighting(String weighting) {
        this.weighting = weighting;
    }

    public FCORE_FeatureModel getFcore_featuremodel() {
        return fcore_featuremodel;
    }

    public void setFcore_featuremodel(FCORE_FeatureModel fcore_featuremodel) {
        this.fcore_featuremodel = fcore_featuremodel;
    }

}