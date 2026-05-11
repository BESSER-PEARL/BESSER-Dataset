





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Environment  {






    private List<tool_ToolEntry> tool_toolentrys;




    private SytemColorsPalette sytemcolorspalette;


    public viewpoint_description_Environment(
    ) {
        this.tool_toolentrys = new ArrayList<>();
    }

    public viewpoint_description_Environment(
        ArrayList<tool_ToolEntry> tool_toolentrys    ) {
        this.tool_toolentrys = tool_toolentrys;
    }


    public List<tool_ToolEntry> getTool_toolentrys() {
        return tool_toolentrys;
    }

    public void addTool_toolentry(Tool_toolentry tool_toolentry) {
        this.tool_toolentrys.add(tool_toolentry);
    }
    public SytemColorsPalette getSytemcolorspalette() {
        return sytemcolorspalette;
    }

    public void setSytemcolorspalette(SytemColorsPalette sytemcolorspalette) {
        this.sytemcolorspalette = sytemcolorspalette;
    }

}