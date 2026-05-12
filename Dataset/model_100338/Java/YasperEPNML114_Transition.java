





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_Transition  {

    private String group;
    private String id;





    private List<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private YasperEPNML114_Net yasperepnml114_net;


    public YasperEPNML114_Transition(
        String group,        String id    ) {
        this.group = group;
        this.id = id;
        this.yasperepnml114_toolspecifictypes = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
    }

    public YasperEPNML114_Transition(
        String group,        String id        ArrayList<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations    ) {
        this.group = group;
        this.id = id;
        this.yasperepnml114_toolspecifictypes = yasperepnml114_toolspecifictypes;
        this.yasperepnml114_pnmlannotations = yasperepnml114_pnmlannotations;
        this.yasperepnml114_pnmlannotations = yasperepnml114_pnmlannotations;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<YasperEPNML114_ToolspecificType> getYasperepnml114_toolspecifictypes() {
        return yasperepnml114_toolspecifictypes;
    }

    public void addYasperepnml114_toolspecifictype(Yasperepnml114_toolspecifictype yasperepnml114_toolspecifictype) {
        this.yasperepnml114_toolspecifictypes.add(yasperepnml114_toolspecifictype);
    }
    public List<YasperEPNML114_PnmlAnnotation> getYasperepnml114_pnmlannotations() {
        return yasperepnml114_pnmlannotations;
    }

    public void addYasperepnml114_pnmlannotation(Yasperepnml114_pnmlannotation yasperepnml114_pnmlannotation) {
        this.yasperepnml114_pnmlannotations.add(yasperepnml114_pnmlannotation);
    }
    public List<YasperEPNML114_PnmlAnnotation> getYasperepnml114_pnmlannotations() {
        return yasperepnml114_pnmlannotations;
    }

    public void addYasperepnml114_pnmlannotation(Yasperepnml114_pnmlannotation yasperepnml114_pnmlannotation) {
        this.yasperepnml114_pnmlannotations.add(yasperepnml114_pnmlannotation);
    }
    public YasperEPNML114_Net getYasperepnml114_net() {
        return yasperepnml114_net;
    }

    public void setYasperepnml114_net(YasperEPNML114_Net yasperepnml114_net) {
        this.yasperepnml114_net = yasperepnml114_net;
    }

}