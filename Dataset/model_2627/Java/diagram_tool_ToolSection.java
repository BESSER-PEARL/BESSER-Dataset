





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ToolSection extends description_IdentifiedElement, description_DocumentedElement {

    private String icon;



    public diagram_tool_ToolSection(
        String icon    ) {
        super(
        );
        this.icon = icon;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }


}