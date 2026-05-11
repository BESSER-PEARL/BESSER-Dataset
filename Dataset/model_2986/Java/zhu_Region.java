





import java.util.List;
import java.util.ArrayList;

public class zhu_Region  {

    private String name;





    private zhu_Transitions zhu_transitions;




    private zhu_States zhu_states;




    private zhu_TopRegion zhu_topregion;




    private zhu_Region zhu_region;


    public zhu_Region(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public zhu_Transitions getZhu_transitions() {
        return zhu_transitions;
    }

    public void setZhu_transitions(zhu_Transitions zhu_transitions) {
        this.zhu_transitions = zhu_transitions;
    }
    public zhu_States getZhu_states() {
        return zhu_states;
    }

    public void setZhu_states(zhu_States zhu_states) {
        this.zhu_states = zhu_states;
    }
    public zhu_TopRegion getZhu_topregion() {
        return zhu_topregion;
    }

    public void setZhu_topregion(zhu_TopRegion zhu_topregion) {
        this.zhu_topregion = zhu_topregion;
    }
    public zhu_Region getZhu_region() {
        return zhu_region;
    }

    public void setZhu_region(zhu_Region zhu_region) {
        this.zhu_region = zhu_region;
    }

}