





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_GroupMenu extends MenuItemDescription {

    private String locationURI;





    private List<tool_GroupMenuItem> tool_groupmenuitems;


    public viewpoint_tool_GroupMenu(
        String locationURI    ) {
        super(
        );
        this.locationURI = locationURI;
        this.tool_groupmenuitems = new ArrayList<>();
    }

    public viewpoint_tool_GroupMenu(
        String locationURI        ArrayList<tool_GroupMenuItem> tool_groupmenuitems    ) {
        this.locationURI = locationURI;
        this.tool_groupmenuitems = tool_groupmenuitems;
    }

    public String getLocationuri() {
        return locationURI;
    }

    public void setLocationuri(String locationURI) {
        this.locationURI = locationURI;
    }

    public List<tool_GroupMenuItem> getTool_groupmenuitems() {
        return tool_groupmenuitems;
    }

    public void addTool_groupmenuitem(Tool_groupmenuitem tool_groupmenuitem) {
        this.tool_groupmenuitems.add(tool_groupmenuitem);
    }

}