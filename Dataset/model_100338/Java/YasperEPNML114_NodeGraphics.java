





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_NodeGraphics  {

    private String group;





    private List<YasperEPNML114_TwoDimVector> yasperepnml114_twodimvectors;




    private List<YasperEPNML114_TwoDimVector> yasperepnml114_twodimvectors;




    private YasperEPNML114_Transition yasperepnml114_transition;


    public YasperEPNML114_NodeGraphics(
        String group    ) {
        this.group = group;
        this.yasperepnml114_twodimvectors = new ArrayList<>();
        this.yasperepnml114_twodimvectors = new ArrayList<>();
    }

    public YasperEPNML114_NodeGraphics(
        String group        ArrayList<YasperEPNML114_TwoDimVector> yasperepnml114_twodimvectors,        ArrayList<YasperEPNML114_TwoDimVector> yasperepnml114_twodimvectors    ) {
        this.group = group;
        this.yasperepnml114_twodimvectors = yasperepnml114_twodimvectors;
        this.yasperepnml114_twodimvectors = yasperepnml114_twodimvectors;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<YasperEPNML114_TwoDimVector> getYasperepnml114_twodimvectors() {
        return yasperepnml114_twodimvectors;
    }

    public void addYasperepnml114_twodimvector(Yasperepnml114_twodimvector yasperepnml114_twodimvector) {
        this.yasperepnml114_twodimvectors.add(yasperepnml114_twodimvector);
    }
    public List<YasperEPNML114_TwoDimVector> getYasperepnml114_twodimvectors() {
        return yasperepnml114_twodimvectors;
    }

    public void addYasperepnml114_twodimvector(Yasperepnml114_twodimvector yasperepnml114_twodimvector) {
        this.yasperepnml114_twodimvectors.add(yasperepnml114_twodimvector);
    }
    public YasperEPNML114_Transition getYasperepnml114_transition() {
        return yasperepnml114_transition;
    }

    public void setYasperepnml114_transition(YasperEPNML114_Transition yasperepnml114_transition) {
        this.yasperepnml114_transition = yasperepnml114_transition;
    }

}