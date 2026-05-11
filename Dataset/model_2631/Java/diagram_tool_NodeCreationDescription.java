





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_NodeCreationDescription extends MappingBasedToolDescription {

    private String iconPath;





    private List<NodeMapping> nodemappings;




    private List<AbstractNodeMapping> abstractnodemappings;


    public diagram_tool_NodeCreationDescription(
        String iconPath    ) {
        super(
        );
        this.iconPath = iconPath;
        this.nodemappings = new ArrayList<>();
        this.abstractnodemappings = new ArrayList<>();
    }

    public diagram_tool_NodeCreationDescription(
        String iconPath        ArrayList<NodeMapping> nodemappings,        ArrayList<AbstractNodeMapping> abstractnodemappings    ) {
        this.iconPath = iconPath;
        this.nodemappings = nodemappings;
        this.abstractnodemappings = abstractnodemappings;
    }

    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }

    public List<NodeMapping> getNodemappings() {
        return nodemappings;
    }

    public void addNodemapping(Nodemapping nodemapping) {
        this.nodemappings.add(nodemapping);
    }
    public List<AbstractNodeMapping> getAbstractnodemappings() {
        return abstractnodemappings;
    }

    public void addAbstractnodemapping(Abstractnodemapping abstractnodemapping) {
        this.abstractnodemappings.add(abstractnodemapping);
    }

}