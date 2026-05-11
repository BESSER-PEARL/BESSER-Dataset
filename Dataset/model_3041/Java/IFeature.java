





import java.util.List;
import java.util.ArrayList;

public class IFeature  {






    private actions_DeactivateFeatureAction actions_deactivatefeatureaction;




    private actions_GetFeatureStateAction actions_getfeaturestateaction;




    private actions_ActivateFeatureAction actions_activatefeatureaction;


    public IFeature(
    ) {
    }



    public actions_DeactivateFeatureAction getActions_deactivatefeatureaction() {
        return actions_deactivatefeatureaction;
    }

    public void setActions_deactivatefeatureaction(actions_DeactivateFeatureAction actions_deactivatefeatureaction) {
        this.actions_deactivatefeatureaction = actions_deactivatefeatureaction;
    }
    public actions_GetFeatureStateAction getActions_getfeaturestateaction() {
        return actions_getfeaturestateaction;
    }

    public void setActions_getfeaturestateaction(actions_GetFeatureStateAction actions_getfeaturestateaction) {
        this.actions_getfeaturestateaction = actions_getfeaturestateaction;
    }
    public actions_ActivateFeatureAction getActions_activatefeatureaction() {
        return actions_activatefeatureaction;
    }

    public void setActions_activatefeatureaction(actions_ActivateFeatureAction actions_activatefeatureaction) {
        this.actions_activatefeatureaction = actions_activatefeatureaction;
    }

}