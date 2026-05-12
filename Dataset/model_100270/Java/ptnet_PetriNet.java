





import java.util.List;
import java.util.ArrayList;

public class ptnet_PetriNet  {

    private String id;
    private String type;





    private ptnet_Name ptnet_name;




    private ptnet_Name ptnet_name;




    private List<ptnet_ToolInfo> ptnet_toolinfos;




    private ptnet_Page ptnet_page;




    private ptnet_ToolInfo ptnet_toolinfo;




    private List<ptnet_Page> ptnet_pages;




    private ptnet_PetriNetDoc ptnet_petrinetdoc;




    private ptnet_PetriNetDoc ptnet_petrinetdoc;


    public ptnet_PetriNet(
        String id,        String type    ) {
        this.id = id;
        this.type = type;
        this.ptnet_toolinfos = new ArrayList<>();
        this.ptnet_pages = new ArrayList<>();
    }

    public ptnet_PetriNet(
        String id,        String type        ArrayList<ptnet_ToolInfo> ptnet_toolinfos,        ArrayList<ptnet_Page> ptnet_pages    ) {
        this.id = id;
        this.type = type;
        this.ptnet_toolinfos = ptnet_toolinfos;
        this.ptnet_pages = ptnet_pages;
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

    public ptnet_Name getPtnet_name() {
        return ptnet_name;
    }

    public void setPtnet_name(ptnet_Name ptnet_name) {
        this.ptnet_name = ptnet_name;
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
    public ptnet_Page getPtnet_page() {
        return ptnet_page;
    }

    public void setPtnet_page(ptnet_Page ptnet_page) {
        this.ptnet_page = ptnet_page;
    }
    public ptnet_ToolInfo getPtnet_toolinfo() {
        return ptnet_toolinfo;
    }

    public void setPtnet_toolinfo(ptnet_ToolInfo ptnet_toolinfo) {
        this.ptnet_toolinfo = ptnet_toolinfo;
    }
    public List<ptnet_Page> getPtnet_pages() {
        return ptnet_pages;
    }

    public void addPtnet_page(Ptnet_page ptnet_page) {
        this.ptnet_pages.add(ptnet_page);
    }
    public ptnet_PetriNetDoc getPtnet_petrinetdoc() {
        return ptnet_petrinetdoc;
    }

    public void setPtnet_petrinetdoc(ptnet_PetriNetDoc ptnet_petrinetdoc) {
        this.ptnet_petrinetdoc = ptnet_petrinetdoc;
    }
    public ptnet_PetriNetDoc getPtnet_petrinetdoc() {
        return ptnet_petrinetdoc;
    }

    public void setPtnet_petrinetdoc(ptnet_PetriNetDoc ptnet_petrinetdoc) {
        this.ptnet_petrinetdoc = ptnet_petrinetdoc;
    }

}