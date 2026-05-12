





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_PnObject  {

    private String id;





    private pnmlcoremodel_Page pnmlcoremodel_page;




    private pnmlcoremodel_Name pnmlcoremodel_name;




    private List<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos;




    private pnmlcoremodel_ToolInfo pnmlcoremodel_toolinfo;




    private pnmlcoremodel_Name pnmlcoremodel_name;




    private pnmlcoremodel_Page pnmlcoremodel_page;


    public pnmlcoremodel_PnObject(
        String id    ) {
        this.id = id;
        this.pnmlcoremodel_toolinfos = new ArrayList<>();
    }

    public pnmlcoremodel_PnObject(
        String id        ArrayList<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos    ) {
        this.id = id;
        this.pnmlcoremodel_toolinfos = pnmlcoremodel_toolinfos;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public pnmlcoremodel_Name getPnmlcoremodel_name() {
        return pnmlcoremodel_name;
    }

    public void setPnmlcoremodel_name(pnmlcoremodel_Name pnmlcoremodel_name) {
        this.pnmlcoremodel_name = pnmlcoremodel_name;
    }
    public pnmlcoremodel_Page getPnmlcoremodel_page() {
        return pnmlcoremodel_page;
    }

    public void setPnmlcoremodel_page(pnmlcoremodel_Page pnmlcoremodel_page) {
        this.pnmlcoremodel_page = pnmlcoremodel_page;
    }

}