





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_EdgeGraphics  {






    private YasperEPNML114_Arc yasperepnml114_arc;




    private List<YasperEPNML114_TwoDimVector> yasperepnml114_twodimvectors;


    public YasperEPNML114_EdgeGraphics(
    ) {
        this.yasperepnml114_twodimvectors = new ArrayList<>();
    }

    public YasperEPNML114_EdgeGraphics(
        ArrayList<YasperEPNML114_TwoDimVector> yasperepnml114_twodimvectors    ) {
        this.yasperepnml114_twodimvectors = yasperepnml114_twodimvectors;
    }


    public YasperEPNML114_Arc getYasperepnml114_arc() {
        return yasperepnml114_arc;
    }

    public void setYasperepnml114_arc(YasperEPNML114_Arc yasperepnml114_arc) {
        this.yasperepnml114_arc = yasperepnml114_arc;
    }
    public List<YasperEPNML114_TwoDimVector> getYasperepnml114_twodimvectors() {
        return yasperepnml114_twodimvectors;
    }

    public void addYasperepnml114_twodimvector(Yasperepnml114_twodimvector yasperepnml114_twodimvector) {
        this.yasperepnml114_twodimvectors.add(yasperepnml114_twodimvector);
    }

}