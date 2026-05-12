





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_Pnml  {

    private String group;





    private List<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes;


    public YasperEPNML114_Pnml(
        String group    ) {
        this.group = group;
        this.yasperepnml114_toolspecifictypes = new ArrayList<>();
    }

    public YasperEPNML114_Pnml(
        String group        ArrayList<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes    ) {
        this.group = group;
        this.yasperepnml114_toolspecifictypes = yasperepnml114_toolspecifictypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<YasperEPNML114_ToolspecificType> getYasperepnml114_toolspecifictypes() {
        return yasperepnml114_toolspecifictypes;
    }

    public void addYasperepnml114_toolspecifictype(Yasperepnml114_toolspecifictype yasperepnml114_toolspecifictype) {
        this.yasperepnml114_toolspecifictypes.add(yasperepnml114_toolspecifictype);
    }

}