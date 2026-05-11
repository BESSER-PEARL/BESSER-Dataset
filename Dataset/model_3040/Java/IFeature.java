





import java.util.List;
import java.util.ArrayList;

public class IFeature  {






    private actions_ActivateFeatureAction actions_activatefeatureaction;




    private actions_GetFeatureStateAction actions_getfeaturestateaction;


    public IFeature(
    ) {
    }



    public actions_ActivateFeatureAction getActions_activatefeatureaction() {
        return actions_activatefeatureaction;
    }

    public void setActions_activatefeatureaction(actions_ActivateFeatureAction actions_activatefeatureaction) {
        this.actions_activatefeatureaction = actions_activatefeatureaction;
    }
    public actions_GetFeatureStateAction getActions_getfeaturestateaction() {
        return actions_getfeaturestateaction;
    }

    public void setActions_getfeaturestateaction(actions_GetFeatureStateAction actions_getfeaturestateaction) {
        this.actions_getfeaturestateaction = actions_getfeaturestateaction;
    }

}