





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Label  {






    private pnmlcoremodel_Graphics pnmlcoremodel_graphics;




    private pnmlcoremodel_PageLabelProxy pnmlcoremodel_pagelabelproxy;




    private List<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos;




    private pnmlcoremodel_LabelProxy pnmlcoremodel_labelproxy;


    public pnmlcoremodel_Label(
    ) {
        this.pnmlcoremodel_toolinfos = new ArrayList<>();
    }

    public pnmlcoremodel_Label(
        ArrayList<pnmlcoremodel_ToolInfo> pnmlcoremodel_toolinfos    ) {
        this.pnmlcoremodel_toolinfos = pnmlcoremodel_toolinfos;
    }


    public pnmlcoremodel_Graphics getPnmlcoremodel_graphics() {
        return pnmlcoremodel_graphics;
    }

    public void setPnmlcoremodel_graphics(pnmlcoremodel_Graphics pnmlcoremodel_graphics) {
        this.pnmlcoremodel_graphics = pnmlcoremodel_graphics;
    }
    public pnmlcoremodel_PageLabelProxy getPnmlcoremodel_pagelabelproxy() {
        return pnmlcoremodel_pagelabelproxy;
    }

    public void setPnmlcoremodel_pagelabelproxy(pnmlcoremodel_PageLabelProxy pnmlcoremodel_pagelabelproxy) {
        this.pnmlcoremodel_pagelabelproxy = pnmlcoremodel_pagelabelproxy;
    }
    public List<pnmlcoremodel_ToolInfo> getPnmlcoremodel_toolinfos() {
        return pnmlcoremodel_toolinfos;
    }

    public void addPnmlcoremodel_toolinfo(Pnmlcoremodel_toolinfo pnmlcoremodel_toolinfo) {
        this.pnmlcoremodel_toolinfos.add(pnmlcoremodel_toolinfo);
    }
    public pnmlcoremodel_LabelProxy getPnmlcoremodel_labelproxy() {
        return pnmlcoremodel_labelproxy;
    }

    public void setPnmlcoremodel_labelproxy(pnmlcoremodel_LabelProxy pnmlcoremodel_labelproxy) {
        this.pnmlcoremodel_labelproxy = pnmlcoremodel_labelproxy;
    }

}