





import java.util.List;
import java.util.ArrayList;

public class metaModelSM_Transition  {






    private metaModelSM_Region metamodelsm_region;




    private List<metaModelSM_Triggers> metamodelsm_triggerss;


    public metaModelSM_Transition(
    ) {
        this.metamodelsm_triggerss = new ArrayList<>();
    }

    public metaModelSM_Transition(
        ArrayList<metaModelSM_Triggers> metamodelsm_triggerss    ) {
        this.metamodelsm_triggerss = metamodelsm_triggerss;
    }


    public metaModelSM_Region getMetamodelsm_region() {
        return metamodelsm_region;
    }

    public void setMetamodelsm_region(metaModelSM_Region metamodelsm_region) {
        this.metamodelsm_region = metamodelsm_region;
    }
    public List<metaModelSM_Triggers> getMetamodelsm_triggerss() {
        return metamodelsm_triggerss;
    }

    public void addMetamodelsm_triggers(Metamodelsm_triggers metamodelsm_triggers) {
        this.metamodelsm_triggerss.add(metamodelsm_triggers);
    }

}