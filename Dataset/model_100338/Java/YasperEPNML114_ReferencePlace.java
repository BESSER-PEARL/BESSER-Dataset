





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_ReferencePlace  {

    private String group;
    private String id;
    private String ref;





    private List<YasperEPNML114_NodeGraphics> yasperepnml114_nodegraphicss;




    private List<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private List<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations;




    private YasperEPNML114_Page yasperepnml114_page;


    public YasperEPNML114_ReferencePlace(
        String group,        String id,        String ref    ) {
        this.group = group;
        this.id = id;
        this.ref = ref;
        this.yasperepnml114_nodegraphicss = new ArrayList<>();
        this.yasperepnml114_toolspecifictypes = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
        this.yasperepnml114_pnmlannotations = new ArrayList<>();
    }

    public YasperEPNML114_ReferencePlace(
        String group,        String id,        String ref        ArrayList<YasperEPNML114_NodeGraphics> yasperepnml114_nodegraphicss,        ArrayList<YasperEPNML114_ToolspecificType> yasperepnml114_toolspecifictypes,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations,        ArrayList<YasperEPNML114_PnmlAnnotation> yasperepnml114_pnmlannotations    ) {
        this.group = group;
        this.id = id;
        this.ref = ref;
        this.yasperepnml114_nodegraphicss = yasperepnml114_nodegraphicss;
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
    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public List<YasperEPNML114_NodeGraphics> getYasperepnml114_nodegraphicss() {
        return yasperepnml114_nodegraphicss;
    }

    public void addYasperepnml114_nodegraphics(Yasperepnml114_nodegraphics yasperepnml114_nodegraphics) {
        this.yasperepnml114_nodegraphicss.add(yasperepnml114_nodegraphics);
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
    public YasperEPNML114_Page getYasperepnml114_page() {
        return yasperepnml114_page;
    }

    public void setYasperepnml114_page(YasperEPNML114_Page yasperepnml114_page) {
        this.yasperepnml114_page = yasperepnml114_page;
    }

}