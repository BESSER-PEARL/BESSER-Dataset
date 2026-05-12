





import java.util.List;
import java.util.ArrayList;

public class hlcorestructure_Label  {






    private hlcorestructure_ToolInfo hlcorestructure_toolinfo;




    private List<hlcorestructure_ToolInfo> hlcorestructure_toolinfos;


    public hlcorestructure_Label(
    ) {
        this.hlcorestructure_toolinfos = new ArrayList<>();
    }

    public hlcorestructure_Label(
        ArrayList<hlcorestructure_ToolInfo> hlcorestructure_toolinfos    ) {
        this.hlcorestructure_toolinfos = hlcorestructure_toolinfos;
    }


    public hlcorestructure_ToolInfo getHlcorestructure_toolinfo() {
        return hlcorestructure_toolinfo;
    }

    public void setHlcorestructure_toolinfo(hlcorestructure_ToolInfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfo = hlcorestructure_toolinfo;
    }
    public List<hlcorestructure_ToolInfo> getHlcorestructure_toolinfos() {
        return hlcorestructure_toolinfos;
    }

    public void addHlcorestructure_toolinfo(Hlcorestructure_toolinfo hlcorestructure_toolinfo) {
        this.hlcorestructure_toolinfos.add(hlcorestructure_toolinfo);
    }

}