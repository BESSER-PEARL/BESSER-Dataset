





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Label  {






    private pnmlcoremodel_ToolInfo pnmlcoremodel_toolinfo;




    private List<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos;


    public pnmlcoremodel_Label(
    ) {
        this.pnmlcoremodel_toolinfos = new ArrayList<>();
    }

    public pnmlcoremodel_Label(
        ArrayList<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos    ) {
        this.pnmlcoremodel_toolinfos = pnmlcoremodel_toolinfos;
    }


    public pnmlcoremodel_ToolInfo getPnmlcoremodel_toolinfo() {
        return pnmlcoremodel_toolinfo;
    }

    public void setPnmlcoremodel_toolinfo(pnmlcoremodel_ToolInfo pnmlcoremodel_toolinfo) {
        this.pnmlcoremodel_toolinfo = pnmlcoremodel_toolinfo;
    }
    public List<pnmlcoremodel_ToolInfo> getPnmlcoremodel_toolinfos() {
        return pnmlcoremodel_toolinfos;
    }

    public void addPnmlcoremodel_toolinfo(Pnmlcoremodel_toolinfo pnmlcoremodel_toolinfo) {
        this.pnmlcoremodel_toolinfos.add(pnmlcoremodel_toolinfo);
    }

}