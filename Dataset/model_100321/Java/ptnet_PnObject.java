





import java.util.List;
import java.util.ArrayList;

public class ptnet_PnObject  {

    private String id;





    private ptnet_Page ptnet_page;




    private ptnet_ToolInfo ptnet_toolinfo;




    private ptnet_Name ptnet_name;




    private ptnet_Page ptnet_page;




    private ptnet_Name ptnet_name;




    private List<ptnet_ToolInfo> ptnet_toolinfos;


    public ptnet_PnObject(
        String id    ) {
        this.id = id;
        this.ptnet_toolinfos = new ArrayList<>();
    }

    public ptnet_PnObject(
        String id        ArrayList<ptnet_ToolInfo> ptnet_toolinfos    ) {
        this.id = id;
        this.ptnet_toolinfos = ptnet_toolinfos;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

}