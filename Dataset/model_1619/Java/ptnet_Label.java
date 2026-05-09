





import java.util.List;
import java.util.ArrayList;

public class ptnet_Label  {






    private ptnet_ToolInfo ptnet_toolinfo;




    private List<ptnet_ToolInfo> ptnet_toolinfos;


    public ptnet_Label(
    ) {
        this.ptnet_toolinfos = new ArrayList<>();
    }

    public ptnet_Label(
        ArrayList<ptnet_ToolInfo> ptnet_toolinfos    ) {
        this.ptnet_toolinfos = ptnet_toolinfos;
    }


    public ptnet_ToolInfo getPtnet_toolinfo() {
        return ptnet_toolinfo;
    }

    public void setPtnet_toolinfo(ptnet_ToolInfo ptnet_toolinfo) {
        this.ptnet_toolinfo = ptnet_toolinfo;
    }
    public List<ptnet_ToolInfo> getPtnet_toolinfos() {
        return ptnet_toolinfos;
    }

    public void addPtnet_toolinfo(Ptnet_toolinfo ptnet_toolinfo) {
        this.ptnet_toolinfos.add(ptnet_toolinfo);
    }

}