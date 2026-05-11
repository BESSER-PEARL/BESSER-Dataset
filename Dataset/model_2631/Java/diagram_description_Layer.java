





import java.util.List;
import java.util.ArrayList;

public class diagram_description_Layer extends description_EndUserDocumentedElement, description_DocumentedElement, description_IdentifiedElement {

    private String icon;





    private List<tool_ToolSection> tool_toolsections;


    public diagram_description_Layer(
        String icon    ) {
        super(
        );
        this.icon = icon;
        this.tool_toolsections = new ArrayList<>();
    }

    public diagram_description_Layer(
        String icon        ArrayList<tool_ToolSection> tool_toolsections    ) {
        this.icon = icon;
        this.tool_toolsections = tool_toolsections;
    }

    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }

    public List<tool_ToolSection> getTool_toolsections() {
        return tool_toolsections;
    }

    public void addTool_toolsection(Tool_toolsection tool_toolsection) {
        this.tool_toolsections.add(tool_toolsection);
    }

}