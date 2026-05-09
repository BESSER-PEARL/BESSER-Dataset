





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_PnObject  {

    private String id;





    private List<hlcorestructure_ToolInfo> hlcorestructure_toolinfos;




    private hlcorestructure_Page hlcorestructure_page;




    private hlcorestructure_Name hlcorestructure_name;




    private hlcorestructure_Name hlcorestructure_name;




    private hlcorestructure_ToolInfo hlcorestructure_toolinfo;




    private hlcorestructure_Page hlcorestructure_page;


    public hlcorestructure_PnObject(
        String id    ) {
        this.id = id;
        this.hlcorestructure_toolinfos = new ArrayList<>();
    }

    public hlcorestructure_PnObject(
        String id        ArrayList<hlcorestructure_ToolInfo> hlcorestructure_toolinfos    ) {
        this.id = id;
        this.hlcorestructure_toolinfos = hlcorestructure_toolinfos;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<hlcorestructure_ToolInfo> getHlcorestructure_toolinfos() {
        return hlcorestructure_toolinfos;
    }

    public void addHlcorestructure_toolinfo(Hlcorestructure_toolinfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfos.add(hlcorestructure_toolinfo);
    }
    public hlcorestructure_Page getHlcorestructure_page() {
        return hlcorestructure_page;
    }

    public void setHlcorestructure_page(hlcorestructure_Page hlcorestructure_page) {
        this.hlcorestructure_page = hlcorestructure_page;
    }
    public hlcorestructure_Name getHlcorestructure_name() {
        return hlcorestructure_name;
    }

    public void setHlcorestructure_name(hlcorestructure_Name hlcorestructure_name) {
        this.hlcorestructure_name = hlcorestructure_name;
    }
    public hlcorestructure_Name getHlcorestructure_name() {
        return hlcorestructure_name;
    }

    public void setHlcorestructure_name(hlcorestructure_Name hlcorestructure_name) {
        this.hlcorestructure_name = hlcorestructure_name;
    }
    public hlcorestructure_ToolInfo getHlcorestructure_toolinfo() {
        return hlcorestructure_toolinfo;
    }

    public void setHlcorestructure_toolinfo(hlcorestructure_ToolInfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfo = hlcorestructure_toolinfo;
    }
    public hlcorestructure_Page getHlcorestructure_page() {
        return hlcorestructure_page;
    }

    public void setHlcorestructure_page(hlcorestructure_Page hlcorestructure_page) {
        this.hlcorestructure_page = hlcorestructure_page;
    }

}