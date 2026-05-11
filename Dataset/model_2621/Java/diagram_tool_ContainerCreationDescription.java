





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ContainerCreationDescription extends MappingBasedToolDescription {

    private String iconPath;





    private List<ContainerMapping> containermappings;




    private List<AbstractNodeMapping> abstractnodemappings;


    public diagram_tool_ContainerCreationDescription(
        String iconPath    ) {
        super(
        );
        this.iconPath = iconPath;
        this.containermappings = new ArrayList<>();
        this.abstractnodemappings = new ArrayList<>();
    }

    public diagram_tool_ContainerCreationDescription(
        String iconPath        ArrayList<ContainerMapping> containermappings,        ArrayList<AbstractNodeMapping> abstractnodemappings    ) {
        this.iconPath = iconPath;
        this.containermappings = containermappings;
        this.abstractnodemappings = abstractnodemappings;
    }

    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }

    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }
    public List<AbstractNodeMapping> getAbstractnodemappings() {
        return abstractnodemappings;
    }

    public void addAbstractnodemapping(Abstractnodemapping abstractnodemapping) {
        this.abstractnodemappings.add(abstractnodemapping);
    }

}