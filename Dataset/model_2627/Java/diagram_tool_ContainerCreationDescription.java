





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ContainerCreationDescription extends MappingBasedToolDescription {

    private String iconPath;





    private List<AbstractNodeMapping> abstractnodemappings;




    private List<ContainerMapping> containermappings;


    public diagram_tool_ContainerCreationDescription(
        String iconPath    ) {
        super(
        );
        this.iconPath = iconPath;
        this.abstractnodemappings = new ArrayList<>();
        this.containermappings = new ArrayList<>();
    }

    public diagram_tool_ContainerCreationDescription(
        String iconPath        ArrayList<AbstractNodeMapping> abstractnodemappings,        ArrayList<ContainerMapping> containermappings    ) {
        this.iconPath = iconPath;
        this.abstractnodemappings = abstractnodemappings;
        this.containermappings = containermappings;
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
    public List<ContainerMapping> getContainermappings() {
        return containermappings;
    }

    public void addContainermapping(Containermapping containermapping) {
        this.containermappings.add(containermapping);
    }

}