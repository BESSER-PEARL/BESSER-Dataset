





import java.util.List;
import java.util.ArrayList;

public class actions_DeactivateFeatureAction extends ReconfigurationAction, PostGenerationAction {






    private IFeature ifeature;


    public actions_DeactivateFeatureAction(
    ) {
        super(
        );
    }



    public IFeature getIfeature() {
        return ifeature;
    }

    public void setIfeature(IFeature ifeature) {
        this.ifeature = ifeature;
    }

}