





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_NodeCreationDescription extends MappingBasedToolDescription {

    private String iconPath;





    private List<AbstractNodeMapping> abstractnodemappings;




    private tool_InitialNodeCreationOperation tool_initialnodecreationoperation;




    private List<NodeMapping> nodemappings;


    public diagram_tool_NodeCreationDescription(
        String iconPath    ) {
        super(
        );
        this.iconPath = iconPath;
        this.abstractnodemappings = new ArrayList<>();
        this.nodemappings = new ArrayList<>();
    }

    public diagram_tool_NodeCreationDescription(
        String iconPath        ArrayList<AbstractNodeMapping> abstractnodemappings,        ArrayList<NodeMapping> nodemappings    ) {
        this.iconPath = iconPath;
        this.abstractnodemappings = abstractnodemappings;
        this.nodemappings = nodemappings;
    }

    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }

    public List<AbstractNodeMapping> getAbstractnodemappings() {
        return abstractnodemappings;
    }

    public void addAbstractnodemapping(Abstractnodemapping abstractnodemapping) {
        this.abstractnodemappings.add(abstractnodemapping);
    }
    public tool_InitialNodeCreationOperation getTool_initialnodecreationoperation() {
        return tool_initialnodecreationoperation;
    }

    public void setTool_initialnodecreationoperation(tool_InitialNodeCreationOperation tool_initialnodecreationoperation) {
        this.tool_initialnodecreationoperation = tool_initialnodecreationoperation;
    }
    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }

}