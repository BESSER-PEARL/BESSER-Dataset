





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_MenuItemDescription extends tool_MenuItemOrRef, tool_AbstractToolDescription {

    private String icon;



    public viewpoint_tool_MenuItemDescription(
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