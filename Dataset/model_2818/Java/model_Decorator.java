





import java.util.List;
import java.util.ArrayList;

public class model_Decorator  {






    private model_Link model_link;




    private model_FeatureContainer model_featurecontainer;


    public model_Decorator(
    ) {
    }



    public model_Link getModel_link() {
        return model_link;
    }

    public void setModel_link(model_Link model_link) {
        this.model_link = model_link;
    }
    public model_FeatureContainer getModel_featurecontainer() {
        return model_featurecontainer;
    }

    public void setModel_featurecontainer(model_FeatureContainer model_featurecontainer) {
        this.model_featurecontainer = model_featurecontainer;
    }

}