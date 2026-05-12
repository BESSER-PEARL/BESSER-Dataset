





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_Page  {

    private String group;
    private String id;





    private List<YasperEPNML114_PlaceType1> yasperepnml114_placetype1s;




    private YasperEPNML114_Net yasperepnml114_net;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private List<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes;




    private List<YasperEPNML114_Transition> yasperepnml114_transitions;




    private List<YasperEPNML114_Page> yasperepnml114_pages;




    private List<YasperEPNML114_Arc> yasperepnml114_arcs;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private List<YasperEPNML114_NetGraphics> yasperepnml114_netgraphicss;


    public YasperEPNML114_Page(
        String group,        String id    ) {
        this.group = group;
        this.id = id;
        this.yasperepnml114_placetype1s = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
        this.yasperepnml114_toolspecifictypes = new ArrayList<>();
        this.yasperepnml114_transitions = new ArrayList<>();
        this.yasperepnml114_pages = new ArrayList<>();
        this.yasperepnml114_arcs = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
        this.yasperepnml114_netgraphicss = new ArrayList<>();
    }

    public YasperEPNML114_Page(
        String group,        String id        ArrayList<YasperEPNML114_PlaceType1> yasperepnml114_placetype1s,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations,        ArrayList<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes,        ArrayList<YasperEPNML114_Transition> yasperepnml114_transitions,        ArrayList<YasperEPNML114_Page> yasperepnml114_pages,        ArrayList<YasperEPNML114_Arc> yasperepnml114_arcs,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations,        ArrayList<YasperEPNML114_NetGraphics> yasperepnml114_netgraphicss    ) {
        this.group = group;
        this.id = id;
        this.yasperepnml114_placetype1s = yasperepnml114_placetype1s;
        this.yasperepnml114_pnmlannotations = yasperepnml114_pnmlannotations;
        this.yasperepnml114_toolspecifictypes = yasperepnml114_toolspecifictypes;
        this.yasperepnml114_transitions = yasperepnml114_transitions;
        this.yasperepnml114_pages = yasperepnml114_pages;
        this.yasperepnml114_arcs = yasperepnml114_arcs;
        this.yasperepnml114_pnmlannotations = yasperepnml114_pnmlannotations;
        this.yasperepnml114_netgraphicss = yasperepnml114_netgraphicss;
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
    public YasperEPNML114_Net getYasperepnml114_net() {
        return yasperepnml114_net;
    }

    public void setYasperepnml114_net(YasperEPNML114_Net yasperepnml114_net) {
        this.yasperepnml114_net = yasperepnml114_net;
    }
    public List<YasperEPNML114_PnmlAnnotation> getYasperepnml114_pnmlannotations() {
        return yasperepnml114_pnmlannotations;
    }

    public void addYasperepnml114_pnmlannotation(Yasperepnml114_pnmlannotation yasperepnml114_pnmlannotation) {
        this.yasperepnml114_pnmlannotations.add(yasperepnml114_pnmlannotation);
    }
    public List<YasperEPNML114_ToolspecificType> getYasperepnml114_toolspecifictypes() {
        return yasperepnml114_toolspecifictypes;
    }

    public void addYasperepnml114_toolspecifictype(Yasperepnml114_toolspecifictype yasperepnml114_toolspecifictype) {
        this.yasperepnml114_toolspecifictypes.add(yasperepnml114_toolspecifictype);
    }
    public List<YasperEPNML114_Transition> getYasperepnml114_transitions() {
        return yasperepnml114_transitions;
    }

    public void addYasperepnml114_transition(Yasperepnml114_transition yasperepnml114_transition) {
        this.yasperepnml114_transitions.add(yasperepnml114_transition);
    }
    public List<YasperEPNML114_Page> getYasperepnml114_pages() {
        return yasperepnml114_pages;
    }

    public void addYasperepnml114_page(Yasperepnml114_page yasperepnml114_page) {
        this.yasperepnml114_pages.add(yasperepnml114_page);
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
    public List<YasperEPNML114_NetGraphics> getYasperepnml114_netgraphicss() {
        return yasperepnml114_netgraphicss;
    }

    public void addYasperepnml114_netgraphics(Yasperepnml114_netgraphics yasperepnml114_netgraphics) {
        this.yasperepnml114_netgraphicss.add(yasperepnml114_netgraphics);
    }

}