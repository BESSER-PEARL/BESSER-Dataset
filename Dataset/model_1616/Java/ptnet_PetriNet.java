





import java.util.List;
import java.util.ArrayList;

public class ptnet_PetriNet  {

    private String type;
    private String id;





    private ptnet_PetriNetDoc ptnet_petrinetdoc;




    private List<ptnet_Page> ptnet_pages;




    private ptnet_ToolInfo ptnet_toolinfo;




    private ptnet_Name ptnet_name;




    private ptnet_Page ptnet_page;




    private ptnet_Name ptnet_name;




    private List<ptnet_ToolInfo> ptnet_toolinfos;




    private ptnet_PetriNetDoc ptnet_petrinetdoc;


    public ptnet_PetriNet(
        String type,        String id    ) {
        this.type = type;
        this.id = id;
        this.ptnet_pages = new ArrayList<>();
        this.ptnet_toolinfos = new ArrayList<>();
    }

    public ptnet_PetriNet(
        String type,        String id        ArrayList<ptnet_Page> ptnet_pages,        ArrayList<ptnet_ToolInfo> ptnet_toolinfos    ) {
        this.type = type;
        this.id = id;
        this.ptnet_pages = ptnet_pages;
        this.ptnet_toolinfos = ptnet_toolinfos;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public ptnet_PetriNetDoc getPtnet_petrinetdoc() {
        return ptnet_petrinetdoc;
    }

    public void setPtnet_petrinetdoc(ptnet_PetriNetDoc ptnet_petrinetdoc) {
        this.ptnet_petrinetdoc = ptnet_petrinetdoc;
    }
    public List<ptnet_Page> getPtnet_pages() {
        return ptnet_pages;
    }

    public void addPtnet_page(Ptnet_page ptnet_page) {
        this.ptnet_pages.add(ptnet_page);
    }
    public ptnet_ToolInfo getPtnet_toolinfo() {
        return ptnet_toolinfo;
    }

    public void setPtnet_toolinfo(ptnet_ToolInfo ptnet_toolinfo) {
        this.ptnet_toolinfo = ptnet_toolinfo;
    }
    public ptnet_Name getPtnet_name() {
        return ptnet_name;
    }

    public void setPtnet_name(ptnet_Name ptnet_name) {
        this.ptnet_name = ptnet_name;
    }
    public ptnet_Page getPtnet_page() {
        return ptnet_page;
    }

    public void setPtnet_page(ptnet_Page ptnet_page) {
        this.ptnet_page = ptnet_page;
    }
    public ptnet_Name getPtnet_name() {
        return ptnet_name;
    }

    public void setPtnet_name(ptnet_Name ptnet_name) {
        this.ptnet_name = ptnet_name;
    }
    public List<ptnet_ToolInfo> getPtnet_toolinfos() {
        return ptnet_toolinfos;
    }

    public void addPtnet_toolinfo(Ptnet_toolinfo ptnet_toolinfo) {
        this.ptnet_toolinfos.add(ptnet_toolinfo);
    }
    public ptnet_PetriNetDoc getPtnet_petrinetdoc() {
        return ptnet_petrinetdoc;
    }

    public void setPtnet_petrinetdoc(ptnet_PetriNetDoc ptnet_petrinetdoc) {
        this.ptnet_petrinetdoc = ptnet_petrinetdoc;
    }

}