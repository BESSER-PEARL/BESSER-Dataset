





import java.util.List;
import java.util.ArrayList;

public class zhu_Transitions  {






    private List<zhu_Transition> zhu_transitions;




    private zhu_TopRegion zhu_topregion;




    private zhu_Transition zhu_transition;




    private zhu_Region zhu_region;


    public zhu_Transitions(
    ) {
        this.zhu_transitions = new ArrayList<>();
    }

    public zhu_Transitions(
        ArrayList<zhu_Transition> zhu_transitions    ) {
        this.zhu_transitions = zhu_transitions;
    }


    public List<zhu_Transition> getZhu_transitions() {
        return zhu_transitions;
    }

    public void addZhu_transition(Zhu_transition zhu_transition) {
        this.zhu_transitions.add(zhu_transition);
    }
    public zhu_TopRegion getZhu_topregion() {
        return zhu_topregion;
    }

    public void setZhu_topregion(zhu_TopRegion zhu_topregion) {
        this.zhu_topregion = zhu_topregion;
    }
    public zhu_Transition getZhu_transition() {
        return zhu_transition;
    }

    public void setZhu_transition(zhu_Transition zhu_transition) {
        this.zhu_transition = zhu_transition;
    }
    public zhu_Region getZhu_region() {
        return zhu_region;
    }

    public void setZhu_region(zhu_Region zhu_region) {
        this.zhu_region = zhu_region;
    }

}