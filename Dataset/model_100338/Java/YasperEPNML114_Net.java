





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_Net  {

    private String type;
    private String group;
    private String id;





    private List<YasperEPNML114_PlaceType1> yasperepnml114_placetype1s;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private List<YasperEPNML114_Arc> yasperepnml114_arcs;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private YasperEPNML114_Pnml yasperepnml114_pnml;




    private List<YasperEPNML114_NetGraphics> yasperepnml114_netgraphicss;




    private List<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes;


    public YasperEPNML114_Net(
        String type,        String group,        String id    ) {
        this.type = type;
        this.group = group;
        this.id = id;
        this.yasperepnml114_placetype1s = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
        this.yasperepnml114_arcs = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
        this.yasperepnml114_netgraphicss = new ArrayList<>();
        this.yasperepnml114_toolspecifictypes = new ArrayList<>();
    }

    public YasperEPNML114_Net(
        String type,        String group,        String id        ArrayList<YasperEPNML114_PlaceType1> yasperepnml114_placetype1s,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations,        ArrayList<YasperEPNML114_Arc> yasperepnml114_arcs,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations,        ArrayList<YasperEPNML114_NetGraphics> yasperepnml114_netgraphicss,        ArrayList<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes    ) {
        this.type = type;
        this.group = group;
        this.id = id;
        this.yasperepnml114_placetype1s = yasperepnml114_placetype1s;
        this.yasperepnml114_pnmlannotations = yasperepnml114_pnmlannotations;
        this.yasperepnml114_arcs = yasperepnml114_arcs;
        this.yasperepnml114_pnmlannotations = yasperepnml114_pnmlannotations;
        this.yasperepnml114_netgraphicss = yasperepnml114_netgraphicss;
        this.yasperepnml114_toolspecifictypes = yasperepnml114_toolspecifictypes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

    public List<YasperEPNML114_PlaceType1> getYasperepnml114_placetype1s() {
        return yasperepnml114_placetype1s;
    }

    public void addYasperepnml114_placetype1(Yasperepnml114_placetype1 yasperepnml114_placetype1) {
        this.yasperepnml114_placetype1s.add(yasperepnml114_placetype1);
    }
    public List<YasperEPNML114_PnmlAnnotation> getYasperepnml114_pnmlannotations() {
        return yasperepnml114_pnmlannotations;
    }

    public void addYasperepnml114_pnmlannotation(Yasperepnml114_pnmlannotation yasperepnml114_pnmlannotation) {
        this.yasperepnml114_pnmlannotations.add(yasperepnml114_pnmlannotation);
    }
    public List<YasperEPNML114_Arc> getYasperepnml114_arcs() {
        return yasperepnml114_arcs;
    }

    public void addYasperepnml114_arc(Yasperepnml114_arc yasperepnml114_arc) {
        this.yasperepnml114_arcs.add(yasperepnml114_arc);
    }
    public List<YasperEPNML114_PnmlAnnotation> getYasperepnml114_pnmlannotations() {
        return yasperepnml114_pnmlannotations;
    }

    public void addYasperepnml114_pnmlannotation(Yasperepnml114_pnmlannotation yasperepnml114_pnmlannotation) {
        this.yasperepnml114_pnmlannotations.add(yasperepnml114_pnmlannotation);
    }
    public YasperEPNML114_Pnml getYasperepnml114_pnml() {
        return yasperepnml114_pnml;
    }

    public void setYasperepnml114_pnml(YasperEPNML114_Pnml yasperepnml114_pnml) {
        this.yasperepnml114_pnml = yasperepnml114_pnml;
    }
    public List<YasperEPNML114_NetGraphics> getYasperepnml114_netgraphicss() {
        return yasperepnml114_netgraphicss;
    }

    public void addYasperepnml114_netgraphics(Yasperepnml114_netgraphics yasperepnml114_netgraphics) {
        this.yasperepnml114_netgraphicss.add(yasperepnml114_netgraphics);
    }
    public List<YasperEPNML114_ToolspecificType> getYasperepnml114_toolspecifictypes() {
        return yasperepnml114_toolspecifictypes;
    }

    public void addYasperepnml114_toolspecifictype(Yasperepnml114_toolspecifictype yasperepnml114_toolspecifictype) {
        this.yasperepnml114_toolspecifictypes.add(yasperepnml114_toolspecifictype);
    }

}