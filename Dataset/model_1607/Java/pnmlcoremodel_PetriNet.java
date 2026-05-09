





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_PetriNet  {

    private String id;
    private String type;





    private pnmlcoremodel_Page pnmlcoremodel_page;




    private pnmlcoremodel_Name pnmlcoremodel_name;




    private pnmlcoremodel_Name pnmlcoremodel_name;




    private List<pnmlcoremodel_Page> pnmlcoremodel_pages;




    private pnmlcoremodel_PetriNetDoc pnmlcoremodel_petrinetdoc;




    private pnmlcoremodel_PetriNetDoc pnmlcoremodel_petrinetdoc;




    private List<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos;




    private pnmlcoremodel_ToolInfo pnmlcoremodel_toolinfo;


    public pnmlcoremodel_PetriNet(
        String id,        String type    ) {
        this.id = id;
        this.type = type;
        this.pnmlcoremodel_pages = new ArrayList<>();
        this.pnmlcoremodel_toolinfos = new ArrayList<>();
    }

    public pnmlcoremodel_PetriNet(
        String id,        String type        ArrayList<pnmlcoremodel_Page> pnmlcoremodel_pages,        ArrayList<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos    ) {
        this.id = id;
        this.type = type;
        this.pnmlcoremodel_pages = pnmlcoremodel_pages;
        this.pnmlcoremodel_toolinfos = pnmlcoremodel_toolinfos;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public pnmlcoremodel_Page getPnmlcoremodel_page() {
        return pnmlcoremodel_page;
    }

    public void setPnmlcoremodel_page(pnmlcoremodel_Page pnmlcoremodel_page) {
        this.pnmlcoremodel_page = pnmlcoremodel_page;
    }
    public pnmlcoremodel_Name getPnmlcoremodel_name() {
        return pnmlcoremodel_name;
    }

    public void setPnmlcoremodel_name(pnmlcoremodel_Name pnmlcoremodel_name) {
        this.pnmlcoremodel_name = pnmlcoremodel_name;
    }
    public pnmlcoremodel_Name getPnmlcoremodel_name() {
        return pnmlcoremodel_name;
    }

    public void setPnmlcoremodel_name(pnmlcoremodel_Name pnmlcoremodel_name) {
        this.pnmlcoremodel_name = pnmlcoremodel_name;
    }
    public List<pnmlcoremodel_Page> getPnmlcoremodel_pages() {
        return pnmlcoremodel_pages;
    }

    public void addPnmlcoremodel_page(Pnmlcoremodel_page pnmlcoremodel_page) {
        this.pnmlcoremodel_pages.add(pnmlcoremodel_page);
    }
    public pnmlcoremodel_PetriNetDoc getPnmlcoremodel_petrinetdoc() {
        return pnmlcoremodel_petrinetdoc;
    }

    public void setPnmlcoremodel_petrinetdoc(pnmlcoremodel_PetriNetDoc pnmlcoremodel_petrinetdoc) {
        this.pnmlcoremodel_petrinetdoc = pnmlcoremodel_petrinetdoc;
    }
    public pnmlcoremodel_PetriNetDoc getPnmlcoremodel_petrinetdoc() {
        return pnmlcoremodel_petrinetdoc;
    }

    public void setPnmlcoremodel_petrinetdoc(pnmlcoremodel_PetriNetDoc pnmlcoremodel_petrinetdoc) {
        this.pnmlcoremodel_petrinetdoc = pnmlcoremodel_petrinetdoc;
    }
    public List<pnmlcoremodel_ToolInfo> getPnmlcoremodel_toolinfos() {
        return pnmlcoremodel_toolinfos;
    }

    public void addPnmlcoremodel_toolinfo(Pnmlcoremodel_toolinfo pnmlcoremodel_toolinfo) {
        this.pnmlcoremodel_toolinfos.add(pnmlcoremodel_toolinfo);
    }
    public pnmlcoremodel_ToolInfo getPnmlcoremodel_toolinfo() {
        return pnmlcoremodel_toolinfo;
    }

    public void setPnmlcoremodel_toolinfo(pnmlcoremodel_ToolInfo pnmlcoremodel_toolinfo) {
        this.pnmlcoremodel_toolinfo = pnmlcoremodel_toolinfo;
    }

}